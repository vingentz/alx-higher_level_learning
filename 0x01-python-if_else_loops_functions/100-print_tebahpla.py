#!/usr/bin/python3
for k in range(122, 96, -1):
    if k % 2 == 0:
        a = k
    else:
        a = k - 32
    print("{}".format(chr(a)), end="")
