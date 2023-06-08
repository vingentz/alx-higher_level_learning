#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    k = len(argv) - 1
    if k == 0:
        print("{} arguments.". format(k))
    elif k == 1:
        print("{} argument:".format(k))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(k))
        m = 1
        for arg in argv[1:]:
            print("{}: {}".format(m, arg))
            m += 1
