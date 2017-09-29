#!/usr/bin/python
import sys

def main(filename=sys.argv[1], N=int(sys.argv[2])):
    """Find the N longest lines in filename and write to filename + ".new"
    """
    lines = open(filename).readlines()
    lines.sort(cmp=lambda x,y: cmp(len(y), len(x)))
    open(filename+".new", "w").write("".join(lines[:N]))

if __name__ == '__main__':
    main()
