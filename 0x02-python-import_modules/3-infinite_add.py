#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 0
    for arg in argv[1:]:
        num += int(arg)
    print(num)
