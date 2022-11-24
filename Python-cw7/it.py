import itertools
import random

iter1 = itertools.cycle([0, 1])
iter2 = iter(lambda: random.choice(["N", "E", "S", "W"]), 1)
iter3 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

for i in range(10):
    print(next(iter1))

print("\n")

for i in range(10):
    print(next(iter2))

print("\n")

for i in range(14):
    print(next(iter3))

