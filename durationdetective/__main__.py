"""Runs the Module"""

import pathlib
import sys

from .cli import parseArgs
#from .rptree import DirectoryTree
from .durationdetective import DurationDetective


def main():
    args = parseArgs()
    print(args)
    
    path_to_folder = pathlib.Path(args.path_to_folder)
    print(path_to_folder)
    '''
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    
    tree = DirectoryTree(
        root_dir, dir_only=args.dir_only, output_file=args.output_file
    )
    tree.generate()
    '''

    obj = DurationDetective.checkUserInput(path_to_folder)
    obj.run()


if __name__ == "__main__":
    main()
