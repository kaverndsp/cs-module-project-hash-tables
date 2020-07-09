import math

# trade space for time

lookup_table = {}


def inverse_root(n):

    return 1 / math.sqrt(n)


def build():
    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)


build()

print(lookup_table[556])
