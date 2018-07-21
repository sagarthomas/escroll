
from .util import write

from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="")
    parser.add_argument("-i", "--init", help="Creates a file")
    parser.add_argument("-fd", "--find-date",  help="Find all entries at a specific date")
    parser.add_argument("-w", "--write", help="Write a new entry", action="store_true")

    args = parser.parse_args()

    if args.init:
        scroll_file = open("{}.scroll".format(args.init), "w+")
        scroll_file.close()
    elif args.write:
        write()

    ''' Vim code '''
    '''
    
    '''


if __name__ == '__main__':
    main()

