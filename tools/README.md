# Exportar el informe

La fuente es `README.md` y sus imágenes locales. La exportación no descarga recursos externos ni altera el contenido. Los cuadros anchos e imágenes panorámicas se exportan en páginas horizontales; el resto usa A4 vertical. El PDF conserva enlaces web y enlaces internos del índice, y añade marcadores para sus encabezados.

En Windows, con Node 22 o posterior y Python 3.11 o posterior:

```powershell
npm ci
python -m pip install -r requirements-report.txt
npm run export:pdf -- output/pdf/upc-pre-202620-1asi0730-8093-dataflux-report-tb1.pdf python
```

El renderizador usa Arial de `C:/Windows/Fonts`. Si se usa otro sistema, configure las fuentes en `tools/render_report.py`. Un código de salida 2 indica imágenes locales faltantes; revise la lista y corrija la fuente antes de entregar. Revise visualmente tablas y diagramas de la exportación: la generación exitosa no confirma que las evidencias pendientes estén completas.

## Gráficos de colaboración

```powershell
python tools/build-collaboration-charts.py
```

El generador usa los cortes fijos y conteos de `delivery/collaboration-counts.json`, confirmados contra GitHub y el historial sin merges del informe. Sus PNG se almacenan en `assets/tb1-collaboration/`. No recalcula productividad ni calificaciones, y excluye otros repositorios y PRs abiertos. Un corte fijo evita que el commit que añade la figura cambie su propio conteo.
