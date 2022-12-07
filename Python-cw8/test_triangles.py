from typing_extensions import Literal
from Triangle import *
from Point import *
import pytest

def test_str():
    t = Triangle(1, 1, 3, 2, 0, 2)
    t1 = Triangle(0, 5, 6, 0, 0, -4)
    assert str(t) == "[(1, 1), (3, 2), (0, 2)]"
    assert str(t1) == "[(0, 5), (6, 0), (0, -4)]"

def test_repr():
    t = Triangle(1, 1, 3, 2, 0, 2)
    t1 = Triangle(0, 5, 6, 0, 0, -4)
    assert repr(t) == "Triangle(1, 1, 3, 2, 0, 2)"
    assert repr(t1) == "Triangle(0, 5, 6, 0, 0, -4)"

def test_eq():
    t = Triangle(1, 1, 3, 2, 0, 2)
    t1 = Triangle(0, 5, 6, 0, 0, -4)
    assert t.__eq__(t) == True
    assert t1.__eq__(t1) == True


def test_ne():
    t = Triangle(1, 1, 3, 2, 0, 2)
    t1 = Triangle(0, 5, 6, 0, 0, -4)
    assert t.__ne__(Triangle(6, 6, 1, 2, 7, 4)) == True
    assert t1.__ne__(Triangle(6, 6, 1, 2, 7, 4)) == True

def test_area():
    t = Triangle(1, 1, 3, 2, 0, 2)
    t1 = Triangle(0, 5, 6, 0, 0, -4)
    t2 = Triangle(4, 3, 6, 6, 0 , 5)
    assert t.area() == 3.0/2.0
    assert t1.area() == 27.0
    assert t2.area() == 8.0

def test_move():
    t, t1, t2 = Triangle(1, 1, 3, 2, 0, 2), Triangle(0, 5, 6, 0, 0, -4), Triangle(4, 3, 6, 6, 0 , 5)
    t.move(1,1)
    t1.move(2,3)
    t2.move(4,0)
    assert t == Triangle(2, 2, 4, 3, 1, 3)
    assert t1 == Triangle(2, 8 , 8, 3, 2, -1)
    assert t2 == Triangle(8, 3, 10, 6, 4, 5)

def test_make4():
  
    kr = Triangle(0, 0, 2, 4, 4, 0).make4()
    t1 = kr[0]
    t2 = kr[1]
    t3 = kr[2]
    t4 = kr[3]
    assert t1 == Triangle(0,0,1,2,2,0)
    assert t2 == Triangle(1,2,2,4,3,2)
    assert t3 == Triangle(3,2,4,0,2,0)
    assert t4 == Triangle(1,2,3,2,2,0)
    assert t1.area() == t2.area()
    assert t2.area() == t3.area()
    assert t3.area() == t4.area()

def test_top():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.top == 2

def test_left():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.left == 0

def test_right():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.right == 3

def test_bottom():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.bottom == 1

def test_width():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.width == 1

def test_height():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.height == 1

def test_topleft():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.topleft == Point(0, 2)

def test_topright():
    t = Triangle(1, 1, 3, 2, 0, 2)
    assert t.topright == Point(3, 2)

def test_bottomleft():
    t = Triangle(1, 1, 3, 2, 0 ,2)
    assert t.bottomleft == Point(0, 1)

def test_bottomright():
    t = Triangle(1, 1, 3, 2, 0 , 2)
    assert t.bottomright == Point(3, 1)

def test_from_points():
    t = Triangle.from_points((Point(1, 1), Point(3, 2), Point(0, 2)))
    assert str(t) == "[(1, 1), (3, 2), (0, 2)]"


if __name__ == "__main__":
    pytest.main()
