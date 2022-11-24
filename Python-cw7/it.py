# Laboratorium nr. 7
# Zad. 7.6

# Stworzyc nastepujace iteratory nieskonczone:
# (a) zwracajacy 0, 1, 0, 1, 0, 1, ...,
# (b) zwracajacy przypadkowo jedna wartosc z ("N", "E", "S", "W") [bladzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracajacy 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import itertools
import random

iter1 = itertools.cycle([0, 1]) # (a)
iter2 = iter(lambda: random.choice(["N", "E", "S", "W"]), 1) # (b)
iter3 = itertools.cycle([0, 1, 2, 3, 4, 5, 6]) # (c)

for i in range(10):
    print(next(iter1))

print("\n")

for i in range(10):
    print(next(iter2))

print("\n")

for i in range(14):
    print(next(iter3))

