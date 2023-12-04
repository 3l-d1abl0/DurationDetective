"""Handles the user input via CLI"""

import argparse
import sys

from . import __version__


def parseArgs():
    parser = argparse.ArgumentParser(
        prog="durationdetective",
        description="A Tree-like tool, but for audio/video files",
        epilog="Thanks for using Duration Detective",
    )

    parser.version = f"Duration Detective v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
            "-p",
            "--path-to-folder",
            required=True,
            help=" \"path\" to target folder (absolute Path)"
    )

    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="save it to some file",
    )

    return parser.parse_args()