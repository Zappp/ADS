import math


def euclid_algorithm(a, b):
    if (b == 0):
        return a, 1, 0
    else:
        d, x, y = euclid_algorithm(b, a % b)
        d, x, y = d, y, x - math.floor(a // b) * y
        return d, x, y


d, x, y = euclid_algorithm(35, 50)
print(x)
print(y)
print(d)
