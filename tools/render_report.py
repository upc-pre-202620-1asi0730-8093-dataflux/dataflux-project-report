"""Render the repository Markdown export without fetching remote resources."""
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from lxml import etree
from PIL import Image as RasterImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, NextPageTemplate, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

ROOT = Path(sys.argv[1]).resolve()
OUTPUT = Path(sys.argv[2]).resolve()
FONT_ROOT = Path('C:/Windows/Fonts')
for name, file in [('Report', 'arial.ttf'), ('Report-Bold', 'arialbd.ttf'), ('Report-Italic', 'ariali.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_ROOT / file)))
pdfmetrics.registerFontFamily('Report', normal='Report', bold='Report-Bold', italic='Report-Italic', boldItalic='Report-Bold')
styles = getSampleStyleSheet()
for style in styles.byName.values():
    style.fontName = 'Report'
styles['BodyText'].fontSize = 9
styles['BodyText'].leading = 13
styles['BodyText'].spaceAfter = 7
styles['Heading1'].fontName = styles['Heading2'].fontName = styles['Heading3'].fontName = 'Report-Bold'
styles['Heading1'].fontSize = 20
styles['Heading1'].leading = 25
styles['Heading2'].fontSize = 15
styles['Heading2'].leading = 20
styles['Heading3'].fontSize = 11.5
styles['Heading3'].leading = 16
styles.add(ParagraphStyle('Cell', parent=styles['BodyText'], fontSize=7.5, leading=10, spaceAfter=0))
styles.add(ParagraphStyle('Center', parent=styles['BodyText'], alignment=TA_CENTER))
styles.add(ParagraphStyle('Caption', parent=styles['BodyText'], fontSize=8, leading=11, textColor=colors.HexColor('#43566b')))
styles.add(ParagraphStyle('CodeBlock', parent=styles['BodyText'], fontSize=7.5, leading=10, backColor=colors.HexColor('#f3f5f8'), borderPadding=7))
PAGE = A4
WIDE = landscape(A4)
MARGIN = 42
story = []
missing = []
current_template = 'portrait'


def clean(text):
    return (text or '').replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '-').replace('\u200b', '')


def inline(node):
    parts = [html.escape(clean(node.text))]
    for child in node:
        tag = child.tag.lower() if isinstance(child.tag, str) else ''
        value = inline(child)
        if tag in ('strong', 'b', 'em', 'i', 'u', 'sup', 'sub'):
            mapped = {'strong': 'b', 'em': 'i'}.get(tag, tag)
            parts.append(f'<{mapped}>{value}</{mapped}>')
        elif tag == 'br':
            parts.append('<br/>')
        elif tag == 'a':
            href = child.get('href', '')
            if href.startswith(('https://', 'http://')):
                parts.append(f'<link href="{html.escape(href, quote=True)}" color="#165ca2">{value}</link>')
            else:
                parts.append(value)
        elif tag == 'img':
            parts.append(html.escape(child.get('alt', '')))
        else:
            parts.append(value)
        parts.append(html.escape(clean(child.tail)))
    return ''.join(parts)


def paragraph(node, name='BodyText'):
    text = inline(node).strip()
    if text:
        if name.startswith('Heading'):
            switch_template('portrait')
        story.append(Paragraph(text, styles[name]))


def switch_template(name):
    global current_template
    if current_template != name:
        if story and isinstance(story[-1], PageBreak):
            story.insert(len(story) - 1, NextPageTemplate(name))
        else:
            story.extend([NextPageTemplate(name), PageBreak()])
        current_template = name


def image_node(node):
    src = unquote(node.get('src', ''))
    path = (ROOT / src).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        missing.append(src)
        story.append(Paragraph('Imagen no disponible: ' + html.escape(src), styles['Caption']))
        return
    if path.suffix.lower() == '.svg':
        # The PDF can use a pre-rendered PNG without changing the canonical SVG.
        path = path.with_suffix('.png')
        if not path.is_file():
            missing.append(src)
            return
    with RasterImage.open(path) as raster:
        width, height = raster.size
    is_wide = width / max(height, 1) > 1.4 and width > 900
    switch_template('landscape' if is_wide else 'portrait')
    page_width, page_height = WIDE if current_template == 'landscape' else PAGE
    ratio = min((page_width - 2 * MARGIN) / width, (page_height - 2 * MARGIN - 35) / height)
    specified_width = re.match(r'^(\d+)(px)?$', node.get('width', ''))
    if specified_width:
        ratio = min(ratio, int(specified_width.group(1)) * 0.75 / width)
    story.append(Image(str(path), width=width * ratio, height=height * ratio, hAlign='CENTER'))
    if node.get('alt'):
        story.append(Paragraph(html.escape(clean(node.get('alt'))), styles['Caption']))
    story.append(Spacer(1, 8))


def table_node(node):
    rows = []
    plain = []
    for row in node.xpath('.//tr'):
        cells = row.xpath('./th|./td')
        if cells:
            rows.append([Paragraph(inline(cell) or ' ', styles['Cell']) for cell in cells])
            plain.append([' '.join(cell.itertext()) for cell in cells])
    if not rows:
        return
    count = max(map(len, rows))
    for row in rows:
        row.extend([Paragraph(' ', styles['Cell'])] * (count - len(row)))
    wide = count >= 5
    switch_template('landscape' if wide else 'portrait')
    available = (WIDE if current_template == 'landscape' else PAGE)[0] - 2 * MARGIN
    weights = []
    for index in range(count):
        lengths = sorted(len(row[index]) for row in plain if index < len(row))
        median = lengths[len(lengths) // 2]
        weights.append(max(8, min(70, median ** 0.55 * 3)))
    widths = [available * value / sum(weights) for value in weights]
    table = Table(rows, colWidths=widths, repeatRows=1, splitByRow=1, splitInRow=1, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5edf6')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7f9fc')]),
        ('GRID', (0, 0), (-1, -1), 0.35, colors.HexColor('#c5ced9')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.extend([table, Spacer(1, 10)])


def walk(node):
    tag = node.tag.lower() if isinstance(node.tag, str) else ''
    if tag == 'table':
        table_node(node)
    elif tag == 'img':
        image_node(node)
    elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = min(int(tag[1]), 3)
        if tag == 'h1' and story and not isinstance(story[-1], PageBreak):
            story.append(PageBreak())
        paragraph(node, 'Heading' + str(level))
    elif tag == 'p':
        images = node.xpath('.//img')
        for image in images:
            image_node(image)
        if not images or ''.join(node.itertext()).strip():
            paragraph(node)
    elif tag in ('ul', 'ol'):
        for number, child in enumerate(node, 1):
            bullet = str(number) + '.' if tag == 'ol' else '\u2022'
            text = inline(child).strip()
            if text:
                story.append(Paragraph(text, styles['BodyText'], bulletText=bullet))
    elif tag == 'pre':
        text = html.escape(clean(''.join(node.itertext()))).replace('\n', '<br/>')
        story.append(Paragraph(text or ' ', styles['CodeBlock']))
    elif tag == 'hr':
        story.append(Spacer(1, 10))
    elif tag == 'div' and 'page-break' in node.get('style', ''):
        if story and not isinstance(story[-1], PageBreak):
            story.append(PageBreak())
    else:
        if node.text and node.text.strip():
            story.append(Paragraph(html.escape(clean(node.text)), styles['BodyText']))
        for child in node:
            walk(child)


def footer(canvas, doc):
    width, height = doc.pagesize
    canvas.saveState()
    canvas.setFont('Report', 8)
    canvas.setFillColor(colors.HexColor('#43566b'))
    canvas.drawString(MARGIN, 22, 'DataFlux | RentBuild | TB1 | Fuente: README.md')
    canvas.drawRightString(width - MARGIN, 22, str(doc.page))
    canvas.restoreState()


class ReportDocument(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name.startswith('Heading'):
            key = 'section-' + str(self.seq.nextf('heading'))
            self.canv.bookmarkPage(key)
            # One flat outline avoids invalid jumps between heading levels.
            self.canv.addOutlineEntry(flowable.getPlainText(), key, 0, False)


tree = etree.HTML(sys.stdin.buffer.read(), parser=etree.HTMLParser(encoding='utf-8'))
for node in tree.find('body'):
    walk(node)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = ReportDocument(str(OUTPUT), pagesize=PAGE, title='DataFlux - RentBuild - TB1', author='DataFlux')
templates = []
for name, size in [('portrait', PAGE), ('landscape', WIDE)]:
    frame = Frame(MARGIN, MARGIN, size[0] - 2 * MARGIN, size[1] - 2 * MARGIN, id=name, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    templates.append(PageTemplate(id=name, frames=[frame], pagesize=size, onPage=footer))
doc.addPageTemplates(templates)
doc.build(story)
print(f'Exported {OUTPUT}; missing images: {len(missing)}')
if missing:
    print('\n'.join(missing))
    sys.exit(2)
