# -*- coding: utf-8 -*-
"""Matplotlib style configuration for STKO_to_python plots.

Features
--------
- Protanopia-friendly default color cycle (toggleable)
- Output modes: "screen", "paper", "presentation"
- Palette override accepting:
  * list[str] of colors
  * matplotlib colormap name (str), e.g. "viridis"
  * matplotlib.colors.Colormap object, e.g. plt.cm.tab20
- Optional subsampling of colormaps to a fixed number of colors
"""

from __future__ import annotations

from typing import Final, Iterable, Literal, Sequence

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# ── Palettes ──────────────────────────────────────────────────────────────

MAIN_COLORS: Final[list[str]] = [
    "blue",
    "black",
    "red",
    "gray",
    "#000077",  # deep navy
    "#5E7470",  # slate green-gray
]

EXTENDED_COLORS: Final[list[str]] = [
    # Cool Blues and Teals (dark → light)
    "#2E3B4E",
    "#4A5E7E",
    "#6A8BA3",
    "#8AACBF",
    "#A8C9DC",
    "#C6E5F7",
    "#2F4F4F",
    "#4E6F6F",
    "#6E8F8F",
    "#8EB0B0",
    "#AED1D1",
    # Muted Purples and Violets
    "#3C2F51",
    "#5A4A7A",
    "#7C6799",
    "#9D87B7",
    "#BFA7D5",
    # Muted Reds and Oranges
    "#502F2A",
    "#744E49",
    "#976E69",
    "#BA8E88",
    "#DCCDBF",
    "#5D3C33",
    "#855E52",
    "#B0876F",
    "#CCA695",
    "#E8CCB9",
    # Soft Greens
    "#2F4632",
    "#546E58",
    "#7B977F",
    "#A3BFA7",
    "#CADFD1",
    # Neutrals and Low-Yellows
    "#4D463D",
    "#7A756C",
    "#A19E98",
    "#C6C4BF",
    "#E6E5E2",
    "#F7F6F4",
]

# Protanopia-friendly set (reduced reliance on reds)
PROTANOPIA_SAFE: Final[list[str]] = [
    "#0072B2",  # strong blue
    "#009E73",  # teal green
    "#56B4E9",  # sky blue
    "#F0E442",  # yellow (high contrast)
    "#E69F00",  # orange
    "#999999",  # neutral gray
]

FULL_PALETTE: Final[list[str]] = [*MAIN_COLORS, *EXTENDED_COLORS]

Mode = Literal["screen", "paper", "presentation"]

__all__ = [
    "set_default_plot_params",
    "get_palette",
]


# ── Helpers ───────────────────────────────────────────────────────────────

def get_palette(
    *,
    protanopia_safe: bool = False,
    extra: Iterable[str] | None = None,
) -> list[str]:
    """
    Return the built-in color cycle as a list.

    Parameters
    ----------
    protanopia_safe : bool
        If True, use a reduced, high-contrast palette suitable for protanopia.
    extra : Iterable[str] | None
        Optional extra colors appended at the end.

    """
    base = list(PROTANOPIA_SAFE if protanopia_safe else FULL_PALETTE)
    if extra:
        base.extend(extra)
    return base


def _mode_overrides(mode: Mode) -> dict[str, object]:
    """rcParams overrides per output mode."""
    if mode == "paper":
        return {
            "font.family": "Times New Roman",
            "font.size": 9,
            "lines.linewidth": 1.0,
            "figure.dpi": 300,
            "savefig.dpi": 300,
        }
    if mode == "presentation":
        return {
            "font.family": "Arial",
            "font.size": 14,
            "lines.linewidth": 2.0,
            "figure.dpi": 120,
            "savefig.dpi": 300,
        }
    # screen (default)
    return {}


def _validate_colors(colors: Sequence[str]) -> list[str]:
    """Ensure the sequence contains valid, non-empty color specs."""
    out: list[str] = []
    for c in colors:
        # Convert anything Matplotlib accepts into hex for consistency.
        out.append(mpl.colors.to_hex(c))
    if not out:
        raise ValueError("Resolved palette is empty; provide at least one color.")
    return out


def _subsample_colormap(
    cmap: mpl.colors.Colormap,
    n_colors: int,
) -> list[str]:
    """
    Sample `n_colors` evenly from a colormap and return hex colors.
    """
    if n_colors <= 0:
        raise ValueError("n_colors must be a positive integer.")
    # Avoid sampling endpoints twice for cyclic maps; use inclusive endpoints here.
    xs = np.linspace(0.0, 1.0, num=n_colors)
    return [mpl.colors.to_hex(cmap(x)) for x in xs]


def _resolve_palette(
    palette_override: list[str] | str | mpl.colors.Colormap | None,
    *,
    default_when_none: list[str],
    n_colors: int | None = 20,
) -> list[str]:
    """
    Convert any supported palette_override input into a list of hex colors.

    Parameters
    ----------
    palette_override : list[str] | str | Colormap | None
        - list/tuple of color specs
        - colormap name (string)
        - Colormap object
        - None → use default_when_none
    default_when_none : list[str]
        Palette to use when override is None.
    n_colors : int | None
        If override is a colormap, subsample to this many colors.
        If None, use cmap.N (full resolution).

    """
    if palette_override is None:
        return _validate_colors(default_when_none)

    if isinstance(palette_override, (list, tuple)):
        return _validate_colors(palette_override)

    if isinstance(palette_override, str):
        cmap = plt.get_cmap(palette_override)
        if n_colors is None:
            # use full colormap resolution
            return _validate_colors(
                [mpl.colors.to_hex(cmap(i)) for i in np.linspace(0.0, 1.0, cmap.N)]
            )
        return _validate_colors(_subsample_colormap(cmap, n_colors))

    if isinstance(palette_override, mpl.colors.Colormap):
        if n_colors is None:
            return _validate_colors(
                [mpl.colors.to_hex(palette_override(i))
                 for i in np.linspace(0.0, 1.0, palette_override.N)]
            )
        return _validate_colors(_subsample_colormap(palette_override, n_colors))

    raise TypeError(
        "palette_override must be a list of colors, a colormap name, a Colormap "
        "object, or None."
    )


# ── Public API ────────────────────────────────────────────────────────────

def set_default_plot_params(
    *,
    mode: Mode = "screen",
    activate_color_cycle: bool = True,
    protanopia_safe_cycle: bool = True,
    palette_override: list[str] | str | mpl.colors.Colormap | None = None,
    override_n_colors: int | None = 20,
) -> None:
    """
    Apply project-wide matplotlib style settings.

    Parameters
    ----------
    mode : {"screen","paper","presentation"}
        Tuning for target medium. Adjusts fonts, dpi, and linewidths.
    activate_color_cycle : bool
        If True, set a global color cycle based on the selected palette.
    protanopia_safe_cycle : bool
        If True (and no override), use protanopia-friendly palette.
    palette_override : list[str] | str | Colormap | None
        If provided, this replaces the built-in palette.
        Accepts:
          - list/tuple of colors
          - colormap name (e.g. "viridis")
          - Colormap object (e.g. plt.cm.tab20)
    override_n_colors : int | None
        When using a colormap override, subsample to this many colors.
        Set None to use the full colormap resolution.

    """
    # Base font
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 10
    plt.rcParams["font.stretch"] = "condensed"

    # Grid
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = (200 / 255.0, 200 / 255.0, 200 / 255.0)
    plt.rcParams["grid.linestyle"] = "--"
    plt.rcParams["grid.linewidth"] = 0.5
    plt.rcParams["grid.alpha"] = 0.6

    # Ticks
    plt.rcParams["xtick.minor.visible"] = True
    plt.rcParams["ytick.minor.visible"] = True
    plt.rcParams["xtick.direction"] = "out"
    plt.rcParams["ytick.direction"] = "out"
    plt.rcParams["xtick.major.pad"] = 4
    plt.rcParams["ytick.major.pad"] = 4

    # Spines
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["axes.spines.left"] = True
    plt.rcParams["axes.spines.bottom"] = True

    # Legend
    plt.rcParams["legend.frameon"] = True
    plt.rcParams["legend.facecolor"] = (0.97, 0.97, 0.97)
    plt.rcParams["legend.edgecolor"] = "none"
    plt.rcParams["legend.framealpha"] = 1.0
    plt.rcParams["legend.fancybox"] = False
    plt.rcParams["legend.borderpad"] = 1.10

    # Lines (crisper joins/caps)
    plt.rcParams["lines.solid_joinstyle"] = "round"
    plt.rcParams["lines.solid_capstyle"] = "round"

    # Figure / savefig defaults
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["savefig.transparent"] = False
    plt.rcParams["savefig.facecolor"] = "white"

    # Mode-specific overrides
    plt.rcParams.update(_mode_overrides(mode))

    # Color cycle
    if activate_color_cycle:
        default_palette = get_palette(protanopia_safe=protanopia_safe_cycle)
        palette = _resolve_palette(
            palette_override,
            default_when_none=default_palette,
            n_colors=override_n_colors,
        )
        plt.rcParams["axes.prop_cycle"] = cycler(color=palette)
