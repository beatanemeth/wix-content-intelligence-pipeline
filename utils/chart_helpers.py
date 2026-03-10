from pathlib import Path

OUTPUT_DIR = Path("./charts")


def save_chart(fig, name, prefix="_"):
    """
    Saves a figure with standard settings and a notebook-specific prefix.

    NOTE: This provides a static PNG fallback to bypass 'Unsupported MimeType'
    errors often encountered when rendering interactive plots in
    VS Code / Docker environments.
    """
    # Ensure the directory exists
    path = Path(OUTPUT_DIR)
    path.mkdir(parents=True, exist_ok=True)

    # Construct the final filename
    file_path = path / f"{prefix}{name}.png"

    # Export with high resolution
    fig.savefig(file_path, dpi=300)
    print(f"💾 Chart exported: {file_path}")
