#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    i = len(sys.argv) - 1
    
    arguments = sys.argv

    if i == 0:
        print("{} arguments.".format(i))
    else i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))


    for i in range(1,len(arguments)):
        print("{}: {}").format(i,arguments[i])
