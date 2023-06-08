#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    ar = argv[2]
    p = {"+": add, "-": sub, "*": mul, "/": div}
    if ar not in p:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    y = int(argv[1])
    z = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(y, ar, z, p[ar](y, z)))
