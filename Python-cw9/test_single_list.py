import pytest
from Python_cw9 import *

@pytest.fixture
def setNa():
    return Node(20)

@pytest.fixture
def setNb():
    return Node(5)

@pytest.fixture
def setL1():
    return SingleList()

@pytest.fixture
def setL2():
    l = SingleList()
    l.insert_head(Node(15))
    l.insert_head(Node(20))
    return l

@pytest.fixture
def setL3():
    l = SingleList()
    l.insert_head(Node(1))
    l.insert_head(Node(14))
    l.insert_head(Node(10))
    return l

def test_node_str(setNa, setNb):
    assert str(setNa) == "Data: 20"
    assert str(setNb) == "Data: 5"

def test_is_empty(setL1, setL2):
    assert setL1.is_empty() == True
    assert setL2.is_empty() == False

def test_count(setL1, setL2, setL3):
    assert setL1.count() == 0
    assert setL2.count() == 2
    assert setL3.count() == 3

def test_insert_head(setL1, setL2):
    setL1.insert_head(Node(9))
    setL2.insert_head(Node(2))

    assert setL1.head.data == 9
    assert setL2.head.data == 2

def test_insert_tail(setL1, setL2):
    setL1.insert_tail(Node(9))
    setL2.insert_tail(Node(2))

    assert setL1.tail.data == 9
    assert setL2.tail.data == 2

def test_remove_head(setL2, setL3):
    setL2.remove_head()
    setL3.remove_head()

    assert setL2.head.data == 15
    assert setL3.head.data == 14

def test_remove_tail(setL2, setL3):
    setL2.remove_tail()
    setL3.remove_tail()

    assert setL2.tail.data == 20
    assert setL3.tail.data == 14

def test_join(setL2, setL3):
    setL2.join(setL3)

    assert setL2.count() == 5
    assert setL3.count() == 0

    assert str(setL2) == "20 --> 15 --> 10 --> 14 --> 1"
    assert setL3.head == None

def test_clear(setL2, setL3):
    setL2.clear()
    setL3.clear()

    assert setL2.count() == 0
    assert setL3.count() == 0
    assert setL2.head == None
    assert setL2.tail == None
    assert setL3.head == None
    assert setL3.tail == None

if __name__ == "__main__":
    pytest.main()