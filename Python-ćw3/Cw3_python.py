from distlib.compat import raw_input

# zad. 3.1
# Czy podany kod jest poprawny skladniowo w Pythonie? Jesli nie to dlaczego?

# x = 2; y = 3;
# if (x>y):
#	result = x
# else
#	result = y;
# for i in "axby": if ord(i) < 100: print(i)  --> W tym wypadku aby program dobrze zadzialal nalezy przeniesc instrukcje warunkowa if oraz te instrukcje ktore do niej naleza
#                                                 do linijki nizej i zastosowac odpowiednie wciecie. W ten sposob dajemy znac kompilatorowi pythona ze instrukcja ta
#                                                 nalezy do wczesniejszej petli for. Poza tym kompilator wypisuje
#                                                 duza ilosc ostrzezen jednak mimo to program zadziala tak jak powinien.
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# zad 3.2
# Co jest zlego w kodzie:

# L = [3, 5, 4] ; L = L.sort()
# x, y = 1, 2, 3                --> Po lewej stronie znajduje sie za malo zmiennych. Nalezy dodac zmienna "z" lub usunac z prawej strony jedna z liczb.
# X = 1, 2, 3 ; X[1] = 4        --> Nie mozna sie odwolywac w taki sposob do elementu krotki!
# X = [1, 2, 3] ; X[3] = 4      
# X = "abc" ; X.append("d")     --> Wyzej X jest lista, ale tutaj przypisujemy pod zmienna X string, dlatego nie mozemy wywolac metody append() i kompilator zwraca blad.
# L = list(map(pow, range(8)))  --> W tym wypadku kompilator zglasza blad dotyczacy funkcji pow, w ktorej brakuje nawiasow i argumentu.

# zad. 3.3
# Wypisac w petli liczby od 0 do 30 z wyjatkiem liczb podzielnych przez 3.

def _3_3():
    for i in range(30):
        if ((i+1) % 3) == 0:
            continue
        else:
            print("{}".format(i+1))

# zad 3.4
# Napisac program pobierajacy w petli od uzytkownika liczbe rzeczywista x (typ float) i wypisujacy x oraz trzecia potege x.
# Zatrzymanie programu nastepuje po wpisaniu z klawiatury stop.
# Jezeli uzytkownik wpisze napis zamiast liczby, to program ma wypisac komunikat o bledzie i kontynuowac prace.

def _3_4():
    while 1:
        num = raw_input("Podaj liczbe rzeczywista: ")
        if num == "stop":
            break

        try:
            pom = float(num)
        except ValueError:
            print("Wpisano napis!")
            continue

        pot = pow(float(pom), 3)
        print("x = {}, x^3 = {}".format(num, pot))

# zad 3.5
# Napisac program rysujacy "miarke" o zadanej dlugosci.
# Nalezy prawidlowo obsluzyc liczby skladajace sie z kilku cyfr (ostatnia cyfra liczby ma znajdowac sie pod znakiem kreski pionowej).
# Nalezy zbudowac pelny string, a potem go wypisac.

def _3_5(num):
    s = str("|....")
    for i in range(num-1):
        s += "|...."
    s += "|\n0"

    for i in range(num):
        s += "%5s" % (i+1)

    print(s)

# zad 3.6
# Napis program rysujacy prostkat zbudowany z malych kratek.
# Nalezy zbudowac pelny string, a potem go wypisac.
# Przykladowy prostokat skladajacy sie z 2x4 pol ma postac:
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+

def _3_6(width, length):
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

# Podany fragment pokaze problem z wyswietlaniem list obiektow stworzonych przez uzytkownika,
# jezeli nie zostala zdefiniowana metode __repr__.
# Jezeli zdefiniowano tylko metode __repr__, to zostanie ona uzyta rowniez wtedy, gdy zwykle pracuje __str__()
# Sprawdzic dzialanie kodu jezeli wykomentujemy __str__() lub metode __repr__()

class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

def _3_7():
    time1 = Time(12)
    time2 = Time(3456)
    print("{} {}".format(time1, time2))   # Python wywoluje str()
    print("{}".format([time1, time2]))   # Python wywoluje repr()

# zad 3.7 odp.
# Jezeli wykomentujemy funkcje __str__() to zamiast niej zostanie wywolana funkcja __repr__().
# Przedostatni print() wyswietli to samo co ostatni w tym przypadku.
# Natomiast gdy zakomentujemy funkcje __repr__() zostana wyswietlone adresy obiektow typu Time w pamieci.
# W tym przypadku funkcja __str__() wykona swoje zadanie i wyswietli odpowiednie rzeczy natomiast adresy
# obiektow klasy Time pokaza sie zamiast tego co miala zwracac funkcja __rer__().

def _3_8(arg1, arg2):
    l1 = []
    l2 = []

    for i in range(len(arg1)):
        for j in range(len(arg2)):
            if (arg1[i] == arg2[j]) & ((arg1[i] in l1) == False):
                l1.append(arg1[i])

    for i in range(len(arg1)):
        if(arg1[i] in l2) == False:
            l2.append(arg1[i])
    for i in range(len(arg2)):
        if(arg2[i] in l2) == False:
            l2.append(arg2[i])

    print("a) {}".format(l1))
    print("b) {}".format(l2))

# zad. 3.9
# Mamy dana liste sekwencji (listy lub krotki) roznej dlugosci zawierajacych liczby.
# Znalezc liste zawierajaca sumy liczb z tych sekwencji.
# Przykladowa sekwencja [[], [4], (1,2), [3,4], (5,6,7)], spodziewany wynik [[0, 4, 3, 7, 18]

def _3_9(list):
    result = []

    for i in range(len(list)):
        sum = 0
        for j in range(len(list[i])):
            sum += list[i][j]
        result.append(sum)

    print(result)

# zad. 3.10
# Stworzyc slownik tlumaczacy liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M)
# na liczby arabskie (podac kilka sposobow tworzenia takiego slownika).
# Mile widziany kod tlumaczacy cala liczbe [funkcja roman2init()]

def _3_10(l_rzymska):
    # Pierwszy sposob tworzenia slownika.
    D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # Drugi sposob tworzenia slownika poprzez liste par.
    lista = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]
    D1 = dict(lista)
    # Trzeci sposob tworzenia slownika poprzez sklejenie dwoch slownikow.
    D2 = {"I": 1, "V": 5, "X": 10, "L": 50}
    D3 = {"C": 100, "D": 500, "M": 1000}
    
    D4 = D2.copy()
    D4.update(D3)

    print(D)
    print(D1)
    print(D4)


    if (l_rzymska in D) == True:
        print("Ta liczba w systemie arabskim to: {}".format(D[l_rzymska]))
    else:
        res = 0
        last = 0
        for i in l_rzymska[::-1]: 
            val = D[i]
            if val >= last:
                res += val
                last = val
            else:
                res -= val
    return res


print("=== zad 3.3 ===")
_3_3()
print("\n=== zad 3.4 ===")
_3_4()
print("\n=== zad 3.5 ===")
_3_5(20)
print("\n=== zad 3.6 ===")
print(_3_6(4, 3))
print("\n=== zad 3.7 ===")
_3_7()
print("\n=== zad 3.8 === test 1: ")
znak1 = "aaurommghuuu"
znak2 = "eewruaazvkhu"
_3_8(znak1, znak2)
print("\n=== zad 3.8 === test 2: ")
liczby = "7289099990"
liczby2 = "111205455"
_3_8(liczby, liczby2)
print("\n=== zad 3.9 ===")
lista = [[], [4], (1,2), [3,4], (5,6,7)]
_3_9(lista)
print("\n=== zad 3.10 ===")
print("XCVIII to {} w jezyku arabskim".format(_3_10("XCVIII")))
