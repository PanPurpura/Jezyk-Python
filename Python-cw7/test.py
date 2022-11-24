# Laboratorium nr. 6
# Zad. 6.2

# Modul testujacy klase Point oraz jej zaimplementowane metody.
# Ponizej znajduja sie testy kazdej z opisanych metod klasy Point.

from Point import *
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test__str__(self):
        self.assertEqual(str(Point(2, 5)), "(2, 5)")
        self.assertEqual(str(Point(5, 4)), "(5, 4)")
        self.assertEqual(str(Point(7, 1)), "(7, 1)")

    def test__repr__(self):
        self.assertEqual(repr(Point(2, 5)), "Point(2, 5)")
        self.assertEqual(repr(Point(5, 4)), "Point(5, 4)")
        self.assertEqual(repr(Point(7, 1)), "Point(7, 1)")

    def test__eq__(self):
        self.assertEqual(Point(2, 5).__eq__(Point(2, 5)), True)
        self.assertEqual(Point(5, 4).__eq__(Point(5, 4)), True)

    def test__ne__(self):
        self.assertNotEqual(Point(2, 5).__ne__(Point(4, 3)), False)
        self.assertNotEqual(Point(5, 5).__ne__(Point(1, 2)), False)

    def test__add__(self):
        self.assertEqual(Point(1, 4).__add__(Point(5, 5)), Point(6, 9))
        self.assertEqual(Point(2, 1).__add__(Point(-4, 8)), Point(-2, 9))
        self.assertEqual(Point(-3, -4).__add__(Point(-1, 1)), Point(-4, -3))

    def test__sub__(self):
        self.assertEqual(Point(1, 4).__sub__(Point(5, 5)), Point(-4, -1))
        self.assertEqual(Point(2, 1).__sub__(Point(-4, 8)), Point(6, -7))
        self.assertEqual(Point(-3, -4).__sub__(Point(-1, 1)), Point(-2, -5))

    def test__mul__(self):
        self.assertEqual(Point(1, 4).__mul__(Point(5, 5)), 25)
        self.assertEqual(Point(2, 1).__mul__(Point(-4, 8)), 0)
        self.assertEqual(Point(-3, -4).__mul__(Point(-1, 1)), -1)

    def test_cross(self):
        self.assertEqual(Point(1, 4).cross(Point(5, 5)), -15)
        self.assertEqual(Point(2, 1).cross(Point(-4, 8)), 20)
        self.assertEqual(Point(-3, -4).cross(Point(-1, 1)), -7)

    def test_length(self):
        self.assertEqual(Point(1, 4).length(), math.sqrt(17))
        self.assertEqual(Point(2, 1).length(), math.sqrt(5))
        self.assertEqual(Point(-3, -4).length(), 5)

    def test_hash(self):
        self.assertEqual(Point(1, 4).__hash__(), 1306364750)
        self.assertEqual(Point(2, 1).__hash__(), 1499606158)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy