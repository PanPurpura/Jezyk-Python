# Laboratoria nr. 6

# Zad. 6.2
# W pliku points.py zdefiniowa� klas� Point wraz z potrzebnymi metodami.
# Punkty s� traktowane jak wektory zaczepione w pocz�tku uk�adu wsp�rz�dnych, o ko�cu w po�o�eniu (x, y).
# Napisa� kod testuj�cy modu� points.

import math

class Point:

    # Konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Wypisanie punktu jako (x1, x2).
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # Wypisanie punktu jako Point(x1, x2)
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # Porownywanie dwoch punktow, czy tak na prawde jest to ten sam punkt.
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    # Porownywanie czy podane dwa punkty sa rozne od siebie.
    def __ne__(self, other):
        return not self == other

    # Dodawanie punktow, v1 + v2.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Odejmowanie punktow, v1 - v2.
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Iloczyn skalarny.
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # Iloczyn wektorowy
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # Funkcja obliczajaca dlugosc wektora.
    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    # Funkcja sluzaca do hashowania.
    def __hash__(self):
        return hash((self.x, self.y))