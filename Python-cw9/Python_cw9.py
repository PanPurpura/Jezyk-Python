class Node:
    """Klasa reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Data: {}".format(self.data)  # bardzo ogolnie


class SingleList:
    """Klasa reprezentujaca cala liste jednokierunkowa."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczac za ka¿dym razem
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        if self.count == 0:
            return "Lista pusta"
        else:
            tmp = self.head
            while tmp.next != None:
                s += "{} --> ".format(tmp.data)
                tmp = tmp.next

            s += "{}".format(tmp.data)

        return s

    def is_empty(self):
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie lacza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):
        if self.length == 0:
            raise ValueError("Lista jest pusta")
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            tmp.next = None
            self.tail = tmp
            self.length -= 1
        node.next = None

        return node

    def clear(self):
        while self.length != 0:
            self.remove_head()

    def join(self, other):
        tmp = self.tail
        tmp.next = other.head
        self.length += other.length
        self.tail = other.tail
        other.head = None
        other.length = 0