#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    i = len(sys.argv) - 1
    
    arguments = sys.argv

    print("{} arguments:".format(i))

    for i in range(1,len(arguments)):
        print("{}: {}").format(i,arguments[i])
