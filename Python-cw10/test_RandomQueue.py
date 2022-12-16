import pytest
from RandomQueue import *

@pytest.fixture
def q1():
    return RandomQueue(15)

@pytest.fixture
def q2():
    s = RandomQueue(15)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    return s

@pytest.fixture
def q3():
    s = RandomQueue(15)
    s.insert(1)
    return s

@pytest.fixture
def q4():
    s = RandomQueue(3)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    return s


def test_insert(q1, q3):
    assert q1.show() == ""
    q1.insert(1)
    q1.insert(2)
    assert q1.show() == "1 --> 2 --> "
    q3.insert(4)
    assert q3.show() == "1 --> 4 --> "

def test_remove(q2, q3):
    q3.remove()
    assert q3.show() == ""
    assert q3.length == 0
    assert q2.remove() == 1 or 2 or 3 or 4
    assert q2.length == 3

def test_is_empty(q1, q2, q3):
    assert q1.is_empty() == True
    assert q2.is_empty() == False
    assert q3.is_empty() == False

def test_is_full(q2, q4):
    assert q2.is_full() == False
    assert q4.is_full() == True

def test_clear(q2, q3):
    q2.clear()
    q3.clear()
    assert q2.length == 0
    assert q3.length == 0

if __name__ == "__main__":
    pytest.main()