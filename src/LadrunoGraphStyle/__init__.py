"""
LadrunoGraphStyle: configuración gráfica personalizada para gráficos científicos y estructurales.
"""

import matplotlib.pyplot as plt
from cycler import cycler

# --- Base and primary colors ---
main_colors = [
    'blue',     # standard blue
    'black',    # high contrast
    'red',
    'gray',     # neutral
    '#000077',  # deep navy
    '#5E7470',  # calm slate green-gray
]

def set_default_plot_params():
    """Aplica estilos gráficos personalizados a Matplotlib."""
    
    # --- Extended muted palette ---
    extended_colors = [
        # Cool Blues and Teals
        '#2E3B4E', '#4A5E7E', '#6A8BA3', '#8AACBF', '#A8C9DC',
        '#2F4F4F', '#4E6F6F', '#6E8F8F', '#8EB0B0', '#AED1D1',

        # Purples and Violets
        '#3C2F51', '#5A4A7A', '#7C6799', '#9D87B7', '#BFA7D5',

        # Reds and Oranges
        '#502F2A', '#744E49', '#976E69', '#BA8E88', '#DCCDBF',
        '#5D3C33', '#855E52', '#B0876F', '#CCA695',

        # Greens
        '#2F4632', '#546E58', '#7B977F', '#A3BFA7',

        # Neutrals
        '#4D463D', '#7A756C', '#A19E98', '#C6C4BF'
    ]

    # Combine palettes and apply
    full_palette = main_colors + extended_colors
    # plt.rcParams['axes.prop_cycle'] = cycler('color', full_palette)

    # Font
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.stretch'] = 'condensed'

    # Grid
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = (200/255, 200/255, 200/255)
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = 0.5
    plt.rcParams['grid.alpha'] = 0.6

    # Ticks
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'

    # Spines
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.left'] = True
    plt.rcParams['axes.spines.bottom'] = True

    # Legend
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.facecolor'] = (0.97, 0.97, 0.97)
    plt.rcParams['legend.edgecolor'] = 'none'
    plt.rcParams['legend.framealpha'] = 1.0
    plt.rcParams['legend.fancybox'] = False
    plt.rcParams['legend.borderpad'] = 1.10

    # Figure
    plt.rcParams['figure.dpi'] = 100

__all__ = ["main_colors", "set_default_plot_params"]
