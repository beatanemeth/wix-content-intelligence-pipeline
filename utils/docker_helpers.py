"""
This file contains helper functions to manage workspace paths and execution contexts.

It resolves the "Where am I?" problem common in Jupyter projects, ensuring consistent
importability and relative path behavior when running inside Docker containers or
switching between local and remote kernels in VS Code.
"""

import os
import sys
from pathlib import Path

# List of folders where notebooks live.
# Root is considered the parent of these.
ALLOWED_SUBDIRS = ["ETL", "data_science", "data_get"]


def align_working_dir(target_subdir, quiet=False):
    """
    FUNCTION 1: Context Logic.
    Ensures os.getcwd() matches the folder where the notebook lives.
    This fixes issues with relative data paths like '../data_raw/'.
    """
    current = Path.cwd()

    # If already aligned, return quietly (Idempotent behavior)
    if current.name == target_subdir:
        return

    # Try to find target as child (from root) or sibling (from another subdir)
    child_path = current / target_subdir
    sibling_path = current.parent / target_subdir

    if child_path.exists():
        os.chdir(child_path)
    elif sibling_path.exists():
        os.chdir(sibling_path)

    if not quiet:
        print(f"📂 Working Directory: {os.path.basename(os.getcwd())}/")


def init_sys_path(quiet=True):
    """
    FUNCTION 2: Importability Logic.
    Ensures the project root is in sys.path so 'import utils' works.
    """
    current = Path.cwd()

    # Root identification
    if current.name in ALLOWED_SUBDIRS:
        project_root = current.parent
    else:
        project_root = current

    root_str = str(project_root.resolve())
    if root_str not in sys.path:
        sys.path.append(root_str)
        if not quiet:
            print(f"🚀 Sys.path initialized at root: {os.path.basename(root_str)}")

    return project_root
