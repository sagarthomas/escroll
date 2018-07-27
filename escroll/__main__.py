from .util import write, parsed_args, open_todo, init
import sys

from argparse import ArgumentParser

def main():
    
    args = parsed_args(sys.argv[1:])

    if args.init:
        init(args.init)
    elif args.write:
        write()
    elif args.todo:
        open_todo()
    



if __name__ == '__main__':
    main()

