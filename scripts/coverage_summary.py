"""Summarise how well ISO 27001 covers NIS2 requirements.

Reads data/nis2_iso27001_mapping.csv, prints a coverage table and saves a chart
to outputs/coverage_chart.png.

Usage: python scripts/coverage_summary.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "nis2_iso27001_mapping.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

ORDER = ["Full", "Partial", "Not covered"]
COLORS = {"Full": "#2E7D32", "Partial": "#F9A825", "Not covered": "#C62828"}


def main() -> None:
    df = pd.read_csv(DATA)

    # Coverage count per type (the 10 Art. 21 measures vs. other obligations)
    summary = (
        df.groupby(["type", "coverage"]).size().unstack(fill_value=0).reindex(columns=ORDER, fill_value=0)
    )
    print("\nCoverage of NIS2 requirements by ISO 27001\n")
    print(summary.to_string())

    art21 = df[df["type"] == "Art21 measure"]
    full = (art21["coverage"] == "Full").sum()
    print(f"\nArt. 21(2) measures fully covered: {full} / {len(art21)}")

    print("\nGaps to close:")
    for _, r in df[df["coverage"] != "Full"].iterrows():
        print(f"- {r['nis2_reference']} [{r['coverage']}]: {r['action_to_close_gap']}")

    # Chart: one horizontal bar per requirement, coloured by coverage
    df = df.iloc[::-1]
    labels = df["nis2_reference"] + "  " + df["short_name"]
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.barh(labels, [1] * len(df), color=df["coverage"].map(COLORS))
    for i, cov in enumerate(df["coverage"]):
        ax.text(0.5, i, cov, ha="center", va="center", color="white", fontsize=9, fontweight="bold")
    ax.set_xticks([])
    ax.set_xlim(0, 1)
    for side in ["top", "right", "bottom"]:
        ax.spines[side].set_visible(False)
    ax.set_title("How much of NIS2 does an ISO 27001 ISMS already cover?", loc="left", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT / "coverage_chart.png", dpi=150)
    print(f"\nChart saved to {OUT / 'coverage_chart.png'}")


if __name__ == "__main__":
    main()
