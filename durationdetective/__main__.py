"""Runs the Module"""

import pathlib
import sys

from .cli import parseArgs
#from .rptree import DirectoryTree
from .durationdetective import DurationDetective


def main():
    args = parseArgs()
    
    path_to_folder = pathlib.Path(args.path_to_folder)

    obj = DurationDetective.checkUserInput(path_to_folder)
    obj.run()


if __name__ == "__main__":
    main()
