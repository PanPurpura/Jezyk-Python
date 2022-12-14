import random

class RandomQueue:

    def __init__(self, size):
        self.n = size
        self.length = 0
        self.items = self.n * [None]

    def insert(self, item):  # wstawia element w czasie O(1)
        if self.is_full():
            raise OverflowError("Kolejka jest pelna!")

        self.items[self.length] = item
        self.length += 1

    def remove(self):   # zwraca losowy element w czasie O(1)

        if self.is_empty():
            raise ValueError("Kolejka jest pusta!")

        idx = random.randint(0, self.length-1)

        if self.n - 1 == idx or self.items[idx+1] == None:
            n = self.items[idx]
            self.items[idx] = None
            self.length -= 1
            return n
        else:
            n = self.items[idx]
            self.items[idx] = self.items[self.n-1]
            self.items[self.n-1] = None

        self.length -= 1
        return n


    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.items[self.n-1] != None:
            return True
        else:
            return False

    def clear(self):
        self.items = self.n * [None]
        self.length = 0

    def show(self):
        s = ""
        for i in range(0, self.length):
                s += "{} --> ".format(self.items[i])

        return s