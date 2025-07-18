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

# --- Extended muted palette ---
extended_colors = [
    # ─── Cool Blues and Teals (darker → lighter) ───────────────
    '#2E3B4E',  # deep midnight blue
    '#4A5E7E',  # slate steel blue
    '#6A8BA3',  # foggy blue
    '#8AACBF',  # washed‐out teal
    '#A8C9DC',  # pale arctic blue
    '#C6E5F7',  # icy sky
    
    '#2F4F4F',  # blackened teal
    '#4E6F6F',  # stormy teal
    '#6E8F8F',  # muted sea‐foam
    '#8EB0B0',  # soft blue‐green
    '#AED1D1',  # washed minty
    
    # ─── Muted Purples and Violets (darker → lighter) ─────────
    '#3C2F51',  # deep eggplant
    '#5A4A7A',  # dusky plum
    '#7C6799',  # lavender dusk
    '#9D87B7',  # pastel grape
    '#BFA7D5',  # faded lilac
    
    # ─── Muted Reds and Oranges (darker → lighter) ────────────
    '#502F2A',  # burnt umber
    '#744E49',  # rusty rose
    '#976E69',  # antique terra
    '#BA8E88',  # clay blend
    '#DCCDBF',  # blush adobe
    
    '#5D3C33',  # deep brick
    '#855E52',  # baked clay
    '#B0876F',  # bronze orange
    '#CCA695',  # desert sand
    '#E8CCB9',  # soft peach
    
    # ─── Soft Greens (darker → lighter) ────────────────────────
    '#2F4632',  # forest shadow
    '#546E58',  # muted sage
    '#7B977F',  # eucalyptus
    '#A3BFA7',  # dusty mint
    '#CADFD1',  # pale seafoam
    
    # ─── Neutrals and Low-Yellows (darker → lighter) ───────────
    '#4D463D',  # deep taupe
    '#7A756C',  # stone ash
    '#A19E98',  # pewter gray
    '#C6C4BF',  # whisper gray
    '#E6E5E2',  # soft paper
    '#F7F6F4',  # almost white
]

# --- Combine full color palette and set cycle ---
full_palette = main_colors + extended_colors

def set_default_plot_params():

    # plt.rcParams['axes.prop_cycle'] = cycler('color', full_palette)

    # --- Font settings ---
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.stretch'] = 'condensed'

    # --- Grid appearance ---
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = (200/255, 200/255, 200/255)  # soft gray
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = 0.5
    plt.rcParams['grid.alpha'] = 0.6

    # --- Minor ticks ---
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'

    # --- Axis spines ---
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.left'] = True
    plt.rcParams['axes.spines.bottom'] = True

    # --- Legend (wipeout style) ---
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.facecolor'] = (0.97, 0.97, 0.97)  # light neutral background
    plt.rcParams['legend.edgecolor'] = 'none'
    plt.rcParams['legend.framealpha'] = 1.0
    plt.rcParams['legend.fancybox'] = False
    plt.rcParams['legend.borderpad'] = 1.10

    # --- Figure appearance ---
    plt.rcParams['figure.dpi'] = 100  # screen only

# Activate the style
set_default_plot_params()

