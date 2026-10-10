#!/usr/bin/env python3
"""Helpers to produce DCM-compliant thesis figures with matplotlib.

    import matplotlib.pyplot as plt
    from scripts import figure_style   # or: import figure_style

    figure_style.use_thesis_style()

    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Voltage (mV)")

    figure_style.save_figure(fig, "figures/Python/example")

Both PDF (paper) and PNG (preview) files are written.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

STYLE = Path(__file__).with_name("miemn.mplstyle")


def use_thesis_style() -> None:
    """Activate the compliant matplotlib style."""
    plt.style.use(str(STYLE))


def save_figure(fig, path, *, png: bool = True, pdf: bool = True) -> None:
    """Save ``fig`` to ``path`` as PDF (and optionally PNG).

    The PDF is what you include in the thesis; the PNG is a quick preview.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if pdf:
        fig.savefig(path.with_suffix(".pdf"))
    if png:
        fig.savefig(path.with_suffix(".png"))
