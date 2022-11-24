# Laboratorium nr. 6
# Zad. 6.4

# W pliku triangles.py zdefiniowac klase Triangle wraz z potrzebnymi metodami.
# Trojkat jest okreslony przez podanie trzech wierzcholkow.
# Napisac kod testujacy modul triangles.

from Point import *
import math

class Triangle:
    # Klasa reprezentujaca trojkat na plaszczyz\nie.

    def count_len(x1, y1, x2, y2):
        return math.fabs(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)))

    # Konstruktor
    def __init__(self, x1, y1, x2, y2, x3, y3):
        if self.count_len(x3, y3, x1, y1) + self.count_len(x1, y1, x2, y2) < self.count_len(x2, y2, x3, y3) or self.count_len(x3, y3, x1, y1) + self.count_len(x2, y2, x3, y3) < self.count_len(x1, y1, x2, y3) or self.count_len(x1, y1, x2, y2) + self.count_len(x2, y2, x3, y3) < self.count_len(x3, y3, x1, y1):
               raise ValueError("Nie mozna zbudowac takiego trojkata!!!")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    # Wypisanie trojkata jako [(x1, y1), (x2, y2), (x3, y3)].
    def __str__(self):
        return "[{}, {}, {}]".format(self.pt1, self.pt2, self.pt3)

    # Wypisanie trojkata jako Triangle(x1, y1, x2, y2, x3, y3).
    def __repr__(self):
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    # Porownanie dwoch trojkatow, t == t1.
    def __eq__(self, other):

        if not isinstance(other, Triangle):
            raise ValueError("Other nie jest trojkatem!!!")

        l1 = (self.pt1, self.pt2, self.pt3)
        l2 = (other.pt1, other.pt2, other.pt3)
        return sorted(l1) == sorted(l2)

    # Sprawdzenie czy dwa trojkaty nie sa rowne, t != t1
    def __ne__(self, other):

        if not isinstance(other, Triangle):
            raise ValueError("Other nie jest trojkatem!!!")

        return not self == other

    # Wyznaczanie srodka ciezkosci trojkata.
    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    # Obliczenie pola trojkata ze wspolrzednych jego wierzcholkow.
    def area(self):
        return 0.5*math.fabs((self.pt2.x-self.pt1.x)*(self.pt3.y-self.pt1.y)-(self.pt2.y-self.pt1.y)*(self.pt3.x-self.pt1.x))

    # Przesuniecie trojkata.
    def move(self, x, y):
        p = Point(x, y)
        self.pt1 += p
        self.pt2 += p
        self.pt3 += p

    def make4(self):
        s1 = Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
        s2 = Point((self.pt2.x+self.pt3.x)/2, (self.pt2.y+self.pt3.y)/2)
        s3 = Point((self.pt3.x+self.pt1.x)/2, (self.pt3.y+self.pt1.y)/2)

        kr = (Triangle(self.pt1.x, self.pt1.y, s1.x, s1.y, s3.x, s3.y), Triangle(s1.x, s1.y, self.pt2.x, self.pt2.y, s2.x, s2.y),
              Triangle(s2.x, s2.y, self.pt3.x, self.pt3.y, s3.x, s3.y), Triangle(s1.x, s1.y, s2.x, s2.y, s3.x, s3.y))

        return kr