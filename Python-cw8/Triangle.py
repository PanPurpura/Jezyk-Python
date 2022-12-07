from typing import List, Tuple
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

        if not isinstance(other, Triangle):
            raise ValueError("Other nie jest trojkatem!!!")

        l1 = (self.pt1, self.pt2, self.pt3)
        l2 = (other.pt1, other.pt2, other.pt3)
        return l1 == l2

    # Sprawdzenie czy dwa trojkaty nie sa rowne, t != t1
    def __ne__(self, other):

        if not isinstance(other, Triangle):
            raise ValueError("Other nie jest trojkatem!!!")

        return not self == other

    # Wyznaczanie srodka ciezkosci trojkata.
  #  def center(self):
  #      return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

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

    @classmethod
    def from_points(cls, arg):
        if len(arg) < 3 or len(arg) > 3:
            raise ValueError("Na liscie/krotce znajduje sie za malo/duzo elementow zeby utworzyc trojkat")
        elif not isinstance(arg[0] or arg[1] or arg[2], Point):
            raise ValueError("Elementy listy to nie punkty!")

        return cls(arg[0].x, arg[0].y, arg[1].x, arg[1].y, arg[2].x, arg[2].y)
    @property
    def center(self):
        Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    @property 
    def top(self):
        x = self.pt1.y
        if self.pt2.y > x:
            x = self.pt2.y
        elif self.pt3.y > x:
            x = self.pt3.y

        return x

    @property 
    def right(self):
        x = self.pt1.x
        if self.pt2.x > x:
            x = self.pt2.x
        elif self.pt3.x > x:
            x = self.pt3.x

        return x

    @property
    def left(self):
        x = self.pt1.x
        if self.pt2.x < x:
            x = self.pt2.x
        elif self.pt3.x < x:
            x = self.pt3.x

        return x

    @property 
    def bottom(self):
        x = self.pt1.y
        if self.pt2.y < x:
            x = self.pt2.y
        elif self.pt3.y < x:
            x = self.pt3.y

        return x

    @property
    def width(self):
        return math.fabs((self.pt3.x - self.pt1.x))

    @property 
    def height(self):
        return math.fabs((self.pt2.y - self.pt1.y))

    def bounding_coor(self):
        xmax = self.pt1.x
        ymax = self.pt1.y
        xmin = self.pt1.x
        ymin = self.pt1.y

        if self.pt2.x > xmax:
            xmax = self.pt2.x
        elif self.pt3.x > xmax:
            xmax = self.pt3.x

        if self.pt2.y > ymax:
            ymax = self.pt2.y
        elif self.pt3.y > ymax:
            ymax = self.pt3.y

        if self.pt2.x < xmin:
            xmin = self.pt2.x
        elif self.pt3.x < xmin:
            xmin = self.pt3.x

        if self.pt2.y < ymin:
            ymin = self.pt2.y
        elif self.pt3.y < ymin:
            ymin = self.pt3.y

        return (xmax, ymax, xmin, ymin)

    @property 
    def topleft(self):
        return Point(self.bounding_coor()[2], self.bounding_coor()[1])

    @property 
    def bottomleft(self):
        return Point(self.bounding_coor()[2], self.bounding_coor()[1] - (self.bounding_coor()[1] - self.bounding_coor()[3]))
    
    @property 
    def topright(self):
        return Point(self.bounding_coor()[2]+(self.bounding_coor()[0] - self.bounding_coor()[2]), self.bounding_coor()[1])

    @property 
    def bottomright(self):
        return Point(self.bounding_coor()[2]+(self.bounding_coor()[0] - self.bounding_coor()[2]), self.bounding_coor()[1] - (self.bounding_coor()[1] - self.bounding_coor()[3]))
