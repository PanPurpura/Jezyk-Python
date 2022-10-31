# Cwiczenia nr. 4 - jezyk Python

# Zad. 4.2
# Rozwiazania zadan 3.5 i 3.6 z poprzedniego zestawu zapisac w postaci funkcji, ktore zwracaja pelny string przez return.
# Funkcje nie powinny pytac uzytkownika o dane, tylko korzystac z argumentow.

from typing import Sequence


def _4_2__3_5(num):
    s = str("|....")
    for i in range(num-1):
        s += "|...."
    s += "|\n0"

    for i in range(num):
        s += "%5s" % (i+1)

    return s

def _4_2__3_6(width, length):
    s = "+"

    for k in range(width):
        for i in range(length):
            s += "---+"

        s += "\n|"

        for j in range(length):
            s += "   |"

        s += "\n+"

    for i in range(length):
        s += "---+"

    return s

# Zad. 4.3
# Napisac iteracyjna wersje funkcji factorial(n) obliczajacej silnie.

def _4_3(n):
    res = 1
    if n == 1:
        return 1
    else:
        for i in range(n):
            res *= (i + 1)
    return res

# Zad 4.4
# Napisac iteracyjna wersje funkcji fibonacci(n) obliczajacej n-ty wyraz ciagu Fibonacciego.

def _4_4(n):
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for i in range(n):
            temp = f1
            f1 = f1+f0
            f0 = temp

    return f0

# Zad. 4.5I oraz 4.5R
# Napisac funkcje odwracanie(L, left, right) odwracajaca kolejnosc elementow na liscie od numeru left do right wlacznie.
# Lista jest modyfikowana w miejscu (in place). Rozwazyc wersje iteracyjna i rekurencyjna.

def _4_5I(L, left, right):
    if left < 0 or right > len(L)-1 or left > right:
        print("Zly zakres argumentu left lub right")
        return -1
    while left!=right:
        pom = L[right]
        L[right] = L[left]
        L[left] = pom
        left += 1
        if left == right:
            break;
        else:
            right -= 1

    return L

def _4_5R(L, left, right):

    if left < right:
        pom = L[right]
        L[right] = L[left]
        L[left] = pom
        _4_5R(L, left+1, right-1) 

# Zad. 4.6
# Napisac funkcje sum_seq(sequence) obliczajaca sume liczb zawartych w sekwencji, ktora moze zawierac zagniezdzone podsekwencje.
# Wskazowka: rozwazyc wersje rekurencyjna, a sprawdzanie, czy element jest sekwencja, wykonac przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    res = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            res += sum_seq(i)
        else:
            res += i

    return res

# Zad 4.7
# Mamy dana sekwencje, w ktorej niektore z elementow moga okazac sie podsekwencjami, a takie zagniezdzenia moga sie nakladac do nieograniczonej glebokosci.
# Napisac funkcjc flatten(sequence), ktora zwroci splaszczona liste wszystkich elementow sekwencji. 
# Wskazowka: rozwazyc wersje rekurencyjna, a sprawdzanie czy element jest sekwencja, wykonac przez isinstance(item, (list, tuple)).

def flatten(sequence):
    list_ = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            list_.extend(flatten(i))
        else:
            list_.append(i)

    return list_

# Testowanie wykonanych cwiczen.
print("=== zad. 4.2 ===")
print("String zwracany przez 3.5: \n{}".format(_4_2__3_5(20)))
print("String zwracany przez 3.6: \n{}".format(_4_2__3_6(2, 4)))
print("\n=== zad. 4.3 ===")
print("3! = {}, 5!: {}, 10!: {}, 18!: {}".format(_4_3(3), _4_3(5), _4_3(10), _4_3(18)))
print("\n=== zad. 4.4 ===")
print("f4: {},\nf11: {},\nf17: {}".format(_4_4(4), _4_4(11), _4_4(17)))
print("\n=== zad. 4.5 iteracyjnie ===")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista poczatkowa: {}".format(L))
print("Zmiana indeksow od 1 do 10, pokazanie podanie blednych argumentow. Funkcja uznaje indeks 0!!!: {}".format(_4_5I(L, 0, 10)))
print("Zmiana indeksow od 1 do 5. Funkcja uznaje indeks 0!!!: {}".format(_4_5I(L, 1, 5)))
print("Zmiana indeksow od 4 do 7. Funkcja uznaje indeks 0!!!: {}".format(_4_5I(L, 4, 7)))
print("\n=== zad. 4.5 rekurencyjnie ===")
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista poczatkowa: {}".format(L1))
_4_5R(L1, 1, 5)
print("Zmiana indeksow od 1 do 5. Funkcja uznaje indeks 0!!!: {}".format(L1))
_4_5R(L1, 4, 7)
print("Zmiana indeksow od 4 do 7. Funkcja uznaje indeks 0!!!: {}".format(L1))
print("\n=== zad. 4.6 ===")
sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("Sekwencja: {}".format(sequence))
print("Suma liczb w sekwencji: {}".format(sum_seq(sequence)))
print("\n=== zad. 4.7 ===")
print("Splaszczona lista dla: {} \nwyglada nastepujaco: {}".format(sequence, flatten(sequence)))



