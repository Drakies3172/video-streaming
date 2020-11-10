import functools


def lstSquare(a):
    if a == 0:
        return []
    return lstSquare(a-1) + [str(a*a)]


print(lstSquare(4))
