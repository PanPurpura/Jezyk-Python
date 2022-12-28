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
    + "5. Dodaj wierzcholek                       6. Czy wierzcholek znajduje sie w grafie?\n" \
    + "7. Usun wierzcholek                        8. Dodaj krawedz\n"\
    + "9. Czy krawedz znajduje sie w grafie?      10. Usun krawedz\n"\
    + "11. Sprawdz wage podanej krawedzi          12. Iterator po wierzcholkach grafu\n"\
    + "13. Iterator po wierzcholkach sasiednich   14. Iterator po krawedziach wychodzacych\n"\
    + "15. Iterator po krawedziach przychodzacych 16. Iterator po krawedziach\n"\
    + "17. Zwroc kopie grafu                      18. Zwroc graf transponowany\n"\
    + "19. Zwroc dopelnienie grafu                20. Zwroc podgraf indukowany\n\n"\
    + "                     21. Zakoncz dzialanie programu"
n = int(size)
d = False
if directed == "True":
    d = True

g = Graph(n, d)

while True:
    print(menu)
    c = input("Wybierz opcje: ")
    match c:
        case "1":
            cls()
            print(g.show_matrix())
            print("Wierzcholki: {}".format(g.show_list_of_nodes()))
            print("Krawedzie: {}".format(g.show_list_of_edges()))
        case "2":
            cls()
            print("Liczba wierzcholkow: {} \n".format(g.v()))
        case "3":
            cls()
            print("Liczba krawedzi: {} \n".format(g.e()))
        case "4":
            cls()
            print("Skierowany? {} \n".format(g.is_directed()))
        case "5":
            cls()
            n = int(input("Podaj numer wierzcholka ktory chcesz dodac [0, {}]: ".format(g.n-1)))
            g.add_node(n)
            print("Dodano wierzcholek o numerze: {} \n".format(n))
        case "6":
            cls()
            n = int(input("Podaj numer wierzcholka: "))
            print(g.has_node(n))
            print("\n")
        case "7":
            cls()
            n = int(input("Podaj numer wierzcholka ktory chcesz usunac [0, {}]: ".format(g.n-1)))
            g.del_node(n)
            print("Usunieto wierzcholek o numerze: {} \n".format(n))
        case "8":
            cls()
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s, t, w)
            g.add_edge(ed)
            #del s,t,w
            print("Dodano krawedz: {}".format(ed))
        case "9":
            cls()
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s,t,w)
            print(g.has_edge(ed))
        case "10":
            cls()
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s,t,w)
            g.del_edge(ed)
            print("Usunieto krawedz: ({}, {}, {})".format(s,t,w))
        case "11":
            cls()
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            print("Waga podanej krawedzi to: {}".format(g.weight(s,t)))
        case "12":
            cls()
            it = g.iternodes()
            print("Wierzcholek: {}".format(next(it)))
            while True: 
                try:
                    c = input("Wyswietlic nastepny element? (Tak/Nie): ")
                    match c:
                        case "Tak":
                            print("Wierzcholek: {}".format(next(it)))
                        case "Nie":
                            break
                except StopIteration:
                    print("Koniec elementow")
                    break
        case "13":
            cls()
            node = int(input("Podaj wierzcholek startowy: "))
            it = g.iteradjacent(node)
            #print("Wierzcholek: {}".format(next(it)))
            while True:       
                try:
                    c = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                    match c:
                        case "Tak":
                            print("Wierzcholek: {}".format(next(it)))
                        case "Nie":
                            break
                except StopIteration:
                    print("Koniec elementow")
                    break
        case "14":
            cls()
            node = int(input("Podaj wierzcholek startowy: "))
            it = g.iteroutedges(node)
            #print("Krawedz: {}".format(next(it)))
            while True:     
                try:
                    c = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                    match c:
                        case "Tak":
                            print("Wierzcholek: {}".format(next(it)))
                        case "Nie":
                            break
                except StopIteration:
                    print("Koniec elementow")
                    break
        case "15":
            cls()
            node = int(input("Podaj wierzcholek startowy: "))
            it = g.iterinedges(node)
            #print("Krawedz: {}".format(next(it)))
            while True:
                try:
                    c = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                    match c:
                        case "Tak":
                            print("Wierzcholek: {}".format(next(it)))
                        case "Nie":
                            break
                except StopIteration:
                    print("Koniec elementow")
                    break
        case "16":
            cls()
            it = g.iteredges()
            #print("Krawedz: {}".format(next(it)))
            while True:
                try:
                    c = input("Witaj w menu iteratora! Wyswietlic nastepny element? (Tak/Nie): ")
                    match c:
                        case "Tak":
                            print("Wierzcholek: {}".format(next(it)))
                        case "Nie":
                            break
                except StopIteration:
                    print("Koniec elementow")
                    break
        case "17":
            cls()
            g1 = g.copy()
            print(g1.show_matrix())
            print("Wierzcholki: {}".format(g1.show_list_of_nodes()))
            print("Krawedzie: {}".format(g1.show_list_of_edges()))
        case "18":
            cls()
            g1 = g.transpose()
            print(g1.show_matrix())
            print("Wierzcholki: {}".format(g1.show_list_of_nodes()))
            print("Krawedzie: {}".format(g1.show_list_of_edges()))
        case "19":
            cls()
            g1 = g.complement()
            print(g1.show_matrix())
            print("Wierzcholki: {}".format(g1.show_list_of_nodes()))
            print("Krawedzie: {}".format(g1.show_list_of_edges()))
        case "20":
            cls()
            nodes = []
            while True:
                c = (input("Podaj wierzcholki dla podgrafu indukowanego (stop == koniec): "))
                if c == "stop":
                    break;
                nodes.append(int(c))

            g1 = g.subgraph(nodes)
            print(g1.show_matrix())
            print("Wierzcholki: {}".format(g1.show_list_of_nodes()))
            print("Krawedzie: {}".format(g1.show_list_of_edges()))
        case "21":
            cls()
            print("Konczenie dzialania programu ...")
            sys.exit()