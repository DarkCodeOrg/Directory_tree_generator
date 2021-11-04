import argparse
import pathlib
import sys

from . import __version__
from .dtree import DirectoryTree
#from .dtree import DirCount, FileCount

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("the specified root directory doesnt exist")
        sys.exit()

    tree = DirectoryTree(root_dir)
    tree.generate()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="D tree, a directory tree generator ",
        epilog="Thanks for using Dtree",
    )
    parser.version = f"D tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()


