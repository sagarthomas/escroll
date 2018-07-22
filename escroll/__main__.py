from .util import write, parsed_args
import sys

from argparse import ArgumentParser

def main():
    
    args = parsed_args(sys.argv[1:])

    if args.init:
        scroll_file = open("{}.scroll".format(args.init), "w+")
        scroll_file.close()
    elif args.write:
        write()



if __name__ == '__main__':
    main()

