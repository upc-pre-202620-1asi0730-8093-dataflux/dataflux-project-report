"""Render fixed, auditable report-history cuts; do not infer member grades."""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "delivery/collaboration-counts.json").read_text(encoding="utf-8"))
OUTPUT = ROOT / "assets/tb1-collaboration"
OUTPUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "Arial", "font.size": 13})
for cut in DATA["cuts"]:
    fig, ax = plt.subplots(figsize=(11, 4.8), dpi=170)
    bars = ax.barh(DATA["authors"], cut["counts"], color="#174D78", height=0.52)
    ax.invert_yaxis()
    ax.set_xlim(0, max(cut["counts"]) * 1.18 + 1)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Commits sin merge · solo repositorio del informe")
    ax.set_title(cut["name"] + " — " + str(cut["total"]) + " commits", loc="left", fontsize=19, pad=15)
    ax.grid(axis="x", alpha=0.15)
    ax.set_axisbelow(True)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=10)
    for bar, value in zip(bars, cut["counts"]):
        ax.text(value + 0.35, bar.get_y() + bar.get_height() / 2, str(value), va="center")
    fig.text(0.18, 0.035, "Corte " + cut["revision"] + " · 08/10/2026 · excluye PRs abiertos y otros repositorios", fontsize=10, color="#475569")
    fig.tight_layout(rect=(0, 0.065, 1, 1))
    fig.savefig(OUTPUT / cut["file"], facecolor="white")
    plt.close(fig)
print("Rendered 2 report-history charts from delivery/collaboration-counts.json")
