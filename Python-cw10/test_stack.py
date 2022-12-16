import pytest
from Stack import *

@pytest.fixture
def setS1():
    return Stack(10)

@pytest.fixture
def setS2():
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    return s

@pytest.fixture
def setS3():
    s = Stack(5)
    s.push(1)
    return s

def test_is_empty(setS1, setS2):
    assert setS1.is_empty() == True
    assert setS2.is_empty() == False

def test_is_full(setS1, setS2):
    assert setS1.is_full() == False
    assert setS2.is_full() == False

def test_push(setS1, setS2):
    setS1.push(20)
    assert setS1.items[setS1.n-1] == 20
    setS1.push(19)
    assert setS1.items[setS1.n-1] == 19
    setS2.push(30)
    assert setS2.items[setS2.n-1] == 30

  #  Instrukcja pokazuje ze w przypadku przepelnienia funkcja push wyrzuca wyjatek i odpowiednia informacje.
  #  setS2.push(45)

def test_pop(setS2, setS3):
    assert setS2.pop() == 4
    assert setS2.items[setS2.n-1] == 3
    assert setS3.pop() == 1
    assert setS3.items[setS3.n-1] == None

   # Instrukcja pokazuje ze w przypadku usuwania elementu z pustego stosu pop wyrzuca wyjatek i odpowiednia informacje.
   # setS3.pop()



if __name__ == "__main__":
    pytest.main()
