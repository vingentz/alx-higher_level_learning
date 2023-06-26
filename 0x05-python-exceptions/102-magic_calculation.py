#!/usr/bin/python3
def magic_calculation(a, b):
    final = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception("Too far")
            else:
                final += (a ** b)/k
        except:
            final = b + a
            break
    return final
