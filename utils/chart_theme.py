import matplotlib.pyplot as plt
import seaborn as sns

# 1. Global Color Palette
CUSTOM_PALETTE = {"Article": "#b726c9", "Blog Post": "#2639c9", "Event": "#8ac926"}


def apply_base_style():
    """
    Applies a consistent style to all Matplotlib/Seaborn charts.
    """
    # Set the general Seaborn theme to white
    sns.set_theme(style="white")

    plt.rcParams.update(
        {
            # Font Configuration
            "font.family": "sans-serif",
            "font.sans-serif": ["Open Sans", "Arial", "DejaVu Sans", "sans-serif"],
            # Spines (Removing Top and Right lines)
            "axes.spines.top": False,
            "axes.spines.right": False,
            # Axes and Grid
            "axes.axisbelow": True,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": "#E0E0E0",
            "grid.linestyle": "--",
            "grid.linewidth": 0.8,
            # Main Figure Title (plt.suptitle)
            "figure.titlesize": 18,
            "figure.titleweight": "bold",
            "figure.subplot.top": 0.88,  # Reserves space so suptitle doesn't overlap
            "figure.autolayout": True,  # The same as plt.tight_layout()
            # Subtitle (plt.title)
            "axes.titlesize": 14,
            "axes.titleweight": "medium",
            "axes.titlecolor": "#292929",
            "axes.titlepad": 25,  # Extra breathing room below the title
            "axes.titlelocation": "center",
            # Axis Labels & Ticks
            "axes.labelsize": 14,
            "axes.labelweight": "semibold",
            "axes.labelpad": 10,
            "xtick.major.size": 6,
            "ytick.major.size": 6,
            "xtick.color": "#292929",
            "ytick.color": "#292929",
            # Legend styling
            "legend.fontsize": 12,
            "legend.frameon": True,
            "legend.facecolor": "#F0F0F0",
            "legend.edgecolor": "none",
            "legend.title_fontsize": 14,
        }
    )

    print("🎨 Global plotting style loaded.")
