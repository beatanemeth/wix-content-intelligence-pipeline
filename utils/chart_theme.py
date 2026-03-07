import matplotlib.pyplot as plt
import seaborn as sns

# 1. Consistent Color Palette
CUSTOM_PALETTE = {"Article": "#b726c9", "Blog Post": "#2639c9", "Event": "#8ac926"}


def apply_base_style():
    """
    Applies a consistent style to all Matplotlib/Seaborn charts.
    """

    # Set the general Seaborn theme to white (no grid) for a clean look
    sns.set_theme(style="white")

    plt.rcParams.update(
        {
            # Font Configuration with Fallbacks
            "font.family": "sans-serif",
            "font.sans-serif": ["Open Sans", "Arial", "DejaVu Sans", "sans-serif"],
            # Spines (Removing Top and Right lines)
            "axes.spines.top": False,
            "axes.spines.right": False,
            # Axes and Grid
            "axes.axisbelow": True,  # This puts the grid lines BEHIND your bars
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": "#E0E0E0",
            "grid.linestyle": "--",
            "grid.linewidth": 0.8,
            # Axis Ticks - visible and pointing outward
            "xtick.bottom": True,  # Show ticks on the bottom axis
            "ytick.left": True,  # Show ticks on the left axis
            "xtick.major.size": 6,
            "ytick.major.size": 6,
            "xtick.color": "#292929",
            "ytick.color": "#292929",
            # Main Title (plt.suptitle)
            "figure.titlesize": 20,
            "figure.titleweight": "bold",
            # Subtitle (plt.title)
            "axes.titlesize": 16,
            "axes.titleweight": "medium",
            "axes.titlecolor": "#292929",
            "axes.titlepad": 20,  # Padding between subtitle and plot
            # Axis Labels
            "axes.labelsize": 14,
            "axes.labelweight": "semibold",
            "axes.labelpad": 10,
            # Legend Body
            "legend.fontsize": 11,
            "legend.frameon": True,
            "legend.facecolor": "#F0F0F0",
            "legend.edgecolor": "none",
            "legend.framealpha": 0.9,
            "legend.borderpad": "1",  # Padding between legend content and border
            "legend.borderaxespad": "1",  # Padding between legend and axes
            # Legend Title
            "legend.title_fontsize": 13,
        }
    )

    print("🎨 Global plotting style loaded.")
