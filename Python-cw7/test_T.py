# Laboratorium nr. 7
# Zad. 7.4

# Modul testujacy klase Triangle oraz jej zaimplementowane metody.
# Ponizej znajduja sie testy kazdej z opisanych metod klasy Triangle.

from Point import *
from Triangle import *
import unittest

class TestTriangle(unittest.TestCase):
    
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Triangle(1, 1, 3, 2, 0, 2)), "[(1, 1), (3, 2), (0, 2)]")
        self.assertEqual(str(Triangle(0, 5, 6, 0, 0, -4)), "[(0, 5), (6, 0), (0, -4)]")

    def test_repr(self):
        self.assertEqual(repr(Triangle(1, 1, 3, 2, 0, 2)), "Triangle(1, 1, 3, 2, 0, 2)")
        self.assertEqual(repr(Triangle(0, 5, 6, 0, 0, -4)), "Triangle(0, 5, 6, 0, 0, -4)")

    def test_eq(self):
        self.assertEqual(Triangle(1, 1, 3, 2, 0, 2).__eq__(Triangle(1, 1, 3, 2, 0, 2)), True)
        self.assertEqual(Triangle(0, 5, 6, 0, 0, -4).__eq__(Triangle(0, 5, 6, 0 ,0, -4)), True)

    def test_ne(self):
        self.assertEqual(Triangle(1, 1, 3, 2, 0, 2).__ne__(Triangle(6,6,1,2,7,4)), True)
        self.assertEqual(Triangle(0, 5, 6, 0, 0, -4).__ne__(Triangle(6,6,1,2,7,4)), True)

    def test_center(self):
        self.assertEqual(Triangle(1, 1, 3, 2, 0, 2).center(), Point(4.0/3.0, 5.0/3.0))
        self.assertEqual(Triangle(0, 5, 6, 0, 0, -4).center(), Point(2.0, 1.0/3.0))
        self.assertEqual(Triangle(4, 3, 6, 6, 0, 5).center(), Point(10.0/3, 14.0/3))

    def test_area(self):
        self.assertEqual(Triangle(1, 1, 3, 2, 0, 2).area(), 3.0/2.0)
        self.assertEqual(Triangle(0, 5, 6, 0, 0, -4).area(), 27.0)
        self.assertEqual(Triangle(4, 3, 6, 6, 0, 5).area(), 8.0)

    def test_move(self):
        t, t1, t2 = Triangle(1, 1, 3, 2, 0, 2), Triangle(0, 5, 6, 0, 0, -4), Triangle(4, 3, 6, 6, 0 , 5)
        t.move(1, 1)
        t1.move(2, 3)
        t2.move(4, 0)
        self.assertEqual(t, Triangle(2, 2, 4, 3, 1, 3))
        self.assertEqual(t1, Triangle(2, 8, 8, 3, 2, -1))
        self.assertEqual(t2, Triangle(8, 3, 10, 6, 4, 5))

    def test_make4(self):
        kr = Triangle(0, 0, 2, 4, 4, 0).make4()
        t1 = kr[0]
        t2 = kr[1]
        t3 = kr[2]
        t4 = kr[3]

        self.assertEqual(t1, Triangle(0, 0, 1, 2, 2, 0))
        self.assertEqual(t2, Triangle(1, 2, 2, 4, 3, 2))
        self.assertEqual(t3, Triangle(3, 2, 4, 0, 2 ,0))
        self.assertEqual(t4, Triangle(1, 2, 3, 2, 2, 0))
        self.assertEqual(t1.area(), t2.area())
        self.assertEqual(t2.area(), t3.area())
        self.assertEqual(t3.area(), t4.area())

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy