# -*- coding: utf-8 -*-
"""Example usage of style_config for STKO_to_python plots."""

from __future__ import annotations

from typing import Sequence

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

# Import your style module (adjust the import path/name as needed)
import style_config as st

# ── demo data helpers ─────────────────────────────────────────────────────
def _sine_family(n_series: int = 6, npts: int = 500) -> tuple[np.ndarray, list[np.ndarray]]:
    """Generate a family of sinusoids with varying frequency/phase."""
    x = np.linspace(0.0, 6.0 * np.pi, npts)
    ys: list[np.ndarray] = []
    rng = np.random.default_rng(42)
    for k in range(n_series):
        amp = 1.0 + 0.2 * rng.normal()
        freq = 1.0 + 0.15 * k
        phase = rng.uniform(-0.5 * np.pi, 0.5 * np.pi)
        ys.append(amp * np.sin(freq * x + phase))
    return x, ys


def _apply_extra_style_cycler(
    *,
    linestyles: Sequence[str] = ("-", "--", "-.", ":"),
    markers: Sequence[str] = ("", "o", "s", "^", "D", "x"),
) -> None:
    """
    Combine the current color cycle with linestyle/marker cycles.
    This improves distinguishability when colors repeat.
    """
    # Read current color cycle (already set by set_default_plot_params)
    current = plt.rcParams.get("axes.prop_cycle", cycler(color=["#1f77b4"]))
    # Build extra cycles (they repeat independently)
    style_cyc = cycler(linestyle=list(linestyles))
    marker_cyc = cycler(marker=list(markers))
    # Combine: color + linestyle + marker
    plt.rcParams["axes.prop_cycle"] = current + style_cyc + marker_cyc


# ── demo plotting routine ────────────────────────────────────────────────
def _demo_plot(title: str, filename: str, n_series: int = 8) -> None:
    """Create a simple multi-series line demo and save to disk."""
    x, ys = _sine_family(n_series=n_series)
    fig, ax = plt.subplots(figsize=(6, 4))
    for y in ys:
        ax.plot(x, y, linewidth=1.6)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("response")
    ax.legend([f"series {i+1}" for i in range(len(ys))], ncol=2, frameon=True)
    fig.tight_layout()
    fig.savefig(filename, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    # 1) Default screen mode, protanopia-safe cycle
    st.set_default_plot_params(mode="screen", protanopia_safe_cycle=True)
    _demo_plot("Default (screen) – protanopia-safe", "demo_01_default_screen.png")

    # 2) Paper mode (thinner lines, serif, high DPI), full built-in palette
    st.set_default_plot_params(mode="paper", protanopia_safe_cycle=False)
    _demo_plot("Paper mode – built-in palette", "demo_02_paper_builtin.png")

    # 3) Presentation mode + VIRIDIS override (subsampled to 12 colors)
    st.set_default_plot_params(
        mode="presentation",
        palette_override="viridis",
        override_n_colors=12,  # subsample to avoid 256‑step gradient
    )
    _demo_plot("Presentation – viridis (12 colors)", "demo_03_presentation_viridis.png")

    # 4) Colormap object override (TAB20), full resolution
    st.set_default_plot_params(
        mode="screen",
        palette_override=plt.cm.tab20,
        override_n_colors=None,  # use full cmap resolution
    )
    _demo_plot("Screen – tab20 (full cmap)", "demo_04_tab20_full.png")

    # 5) Custom short list override (+ linestyle/marker cycler)
    st.set_default_plot_params(
        mode="screen",
        palette_override=["#0072B2", "#009E73", "#F0E442", "#56B4E9"],  # blue, teal, yellow, sky
    )
    _apply_extra_style_cycler(
        linestyles=("-", "--", "-.", ":"),
        markers=("", "o", "s", "^", "D", "x"),
    )
    _demo_plot("Custom list + linestyle/marker cycler", "demo_05_custom_plus_styles.png", n_series=10)

    # 6) Protanopia-safe built-in + linestyle/marker (useful for many series)
    st.set_default_plot_params(mode="screen", protanopia_safe_cycle=True)
    _apply_extra_style_cycler()
    _demo_plot(
        "Protanopia-safe + linestyle/marker",
        "demo_06_protanopia_plus_styles.png",
        n_series=14,
    )

    # 7) Quick example: switch to paper mode and save again (same data, different rc)
    st.set_default_plot_params(mode="paper", protanopia_safe_cycle=True)
    _demo_plot("Paper mode – protanopia-safe", "demo_07_paper_protanopia.png")


if __name__ == "__main__":
    main()
