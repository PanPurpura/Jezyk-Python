from ast import While
from edge import *
from graph import *
import sys, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

size = input("Wprowadz wielkosc grafu: ")
directed = input("Czy graf jest skierowany? (True lub False): ")

menu = "\nMenu programu: \n\n"\
    + "1. Pokaz macierz sasiedztwa i listy        2. Liczba wierzcholkow\n" \
    + "3. Liczba krawedzi                         4. Czy graf jest skierowany?\n"\
    + "5. Czy wierzcholek znajduje sie w grafie?  6. Usun wierzcholek\n" \
    + "7. Dodaj krawedz                           8. Czy krawedz znajduje sie w grafie?\n"\
    + "9. Usun krawedz                            10. Sprawdz wage podanej krawedzi\n"\
    + "11. Iterator po wierzcholkach grafu        12. Iterator po wierzcholkach sasiednich\n"\
    + "13. Iterator po krawedziach wychodzacych   14. Iterator po krawedziach przychodzacych\n"\
    + "15. Iterator po krawedziach                16. Zwroc kopie grafu\n"\
    + "17. Zwroc graf transponowany               18. Zwroc dopelnienie grafu\n"\
    + "19. Zwroc podgraf indukowany               20. DFS\n"\
    + "21. BFS                                    22. Zakoncz dzialanie programu\n"

try:
    n = int(size)
    d = False
except ValueError:
    print("Podano bledne dane!!!")
    sys.exit()

if (directed != "True" and directed != "False") :
    raise ValueError("Podano bledne dane!!!")

if directed == "True":
    d = True

g = Graph(n, d)

while True:
    print(menu)
    c = input("Wybierz opcje: ")

    if c == "1":
        cls()
        print(g.show_matrix())
    elif c == "2":
        cls()
        print("Liczba wierzcholkow: {} \n".format(g.v()))
    elif c == "3":
        cls()
        print("Liczba krawedzi: {} \n".format(g.e()))
    elif c == "4":
        cls()
        print("Skierowany? {} \n".format(g.is_directed()))
    elif c == "5":
        cls()
        try:
            n = int(input("Podaj numer wierzcholka ktory chcesz sprawdzic [0, {}]: ".format(g.n-1)))
        except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
        
        print(g.has_node(n))
        print("\n")
    elif c == "6":
         cls()
         try:
            n = int(input("Podaj numer wierzcholka ktory chcesz usunac [0, {}]: ".format(g.n-1)))
         except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
         
         g.del_node(n)
         print("Usunieto polaczenia z wierzcholkiem o numerze: {} \n".format(n))
    elif c == "7":
        cls()
        try:
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
        except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
        ed = Edge(s, t, w)
        g.add_edge(ed)
        print("Dodano krawedz: {}".format(ed))
    elif c == "8":
        cls()
        try:
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
        except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
        ed = Edge(s,t,w)
        print(g.has_edge(ed))
    elif c == "9":
        cls()
        try:
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
        except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
        ed = Edge(s,t,w)
        g.del_edge(ed)
        print("Usunieto krawedz: ({}, {}, {})".format(s,t,w))
    elif c == "10":
        cls()
        try:
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
        except ValueError:
            print("Bledne dane, przekierowanie do menu")
            continue
        ed = Edge(s, t)
        print("Waga podanej krawedzi to: {}".format(g.weight(ed)))
    elif c == "11":
        cls()
        it = g.iternodes()
        print("Wierzcholek: {}".format(next(it)))
        while True: 
            try:
                c1 = input("Wyswietlic nastepny element? (Tak/Nie): ")
                if c1 == "Tak":
                    print("Wierzcholek: {}".format(next(it)))
                elif c1 == "Nie":
                    break
            except StopIteration:
                print("Koniec elementow")
                break
    elif c == "12":
        cls()
        node = int(input("Podaj wierzcholek startowy: "))
        it = g.iteradjacent(node)
        #print("Wierzcholek: {}".format(next(it)))
        while True:       
            try:
                c1 = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                if c1 == "Tak":
                    print("Wierzcholek: {}".format(next(it)))
                elif c1 == "Nie":
                    break
            except StopIteration:
                print("Koniec elementow")
                break
    elif c == "13":
        cls()
        node = int(input("Podaj wierzcholek startowy: "))
        it = g.iteroutedges(node)
        #print("Krawedz: {}".format(next(it)))
        while True:     
            try:
                c1 = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                if c1 == "Tak":
                    print("Wierzcholek: {}".format(next(it)))
                elif c1 == "Nie":
                    break
            except StopIteration:
                print("Koniec elementow")
                break
    elif c == "14":
        cls()
        node = int(input("Podaj wierzcholek startowy: "))
        it = g.iterinedges(node)
        #print("Krawedz: {}".format(next(it)))
        while True:
            try:
                c1 = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                if c1 == "Tak":
                    print("Wierzcholek: {}".format(next(it)))
                elif c1 == "Nie":
                    break
            except StopIteration:
                print("Koniec elementow")
                break
    elif c == "15":
        cls()
        it = g.iteredges()
        #print("Krawedz: {}".format(next(it)))
        while True:
            try:
                c1 = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                if c1 == "Tak":
                    print("Wierzcholek: {}".format(next(it)))
                elif c1 == "Nie":
                            break
            except StopIteration:
                print("Koniec elementow")
                break
    elif c == "16":
        cls()
        g1 = g.copy()
        print(g1.show_matrix())
    elif c == "17":
        cls()
        g1 = g.transpose()
        print(g1.show_matrix())
    elif c == "18":
        cls()
        g1 = g.complement()
        print(g1.show_matrix())
    elif c == "19":
        cls()
        nodes = []
        while True:
            c1 = (input("Podaj wierzcholki dla podgrafu indukowanego (stop == koniec): "))
            if c1 == "stop":
                break;
            try:
                nodes.append(int(c1))
            except ValueError:
                print("Podano bledne dane, obliczanie podgrafu dla podanych wierzcholkow.")
                break;
                    
        g1 = g.subgraph(nodes)
        print(g1.show_matrix())
    elif c == "20":
        cls()
        vis = []
        try:
            node = int(input("Podaj wierzcholek startowy: "))
        except ValueError:
            print("Podano bledne dane, przekierowanie do menu")
            continue
        g.DFS(node, vis)
        print(vis)
    elif c == "21":
        cls()
        vis = []
        queue = []
        try:
            node = int(input("Podaj wierzcholek startowy: "))
        except ValueError:
            print("Podano bledne dane, przekierowanie do menu")
            continue
        g.BFS(node, vis, queue)
        print(vis)
    elif c == "22":
        cls()
        print("Konczenie dzialania programu ...")
        sys.exit()