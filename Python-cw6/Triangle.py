# Laboratorium nr. 6
# Zad. 6.4

# W pliku triangles.py zdefiniowac klase Triangle wraz z potrzebnymi metodami.
# Trojkat jest okreslony przez podanie trzech wierzcholkow.
# Napisac kod testujacy modul triangles.

from Point import *
import math

class Triangle:
    # Klasa reprezentujaca trojkat na plaszczyz\nie.

    # Konstruktor
    def __init__(self, x1, y1, x2, y2, x3, y3):
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
        l1 = (self.pt1, self.pt2, self.pt3)
        l2 = (other.pt1, other.pt2, other.pt3)
        return l1 == l2

    # Sprawdzenie czy dwa trojkaty nie sa rowne, t != t1
    def __ne__(self, other):
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