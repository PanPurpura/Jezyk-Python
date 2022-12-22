'''
# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,600))

    blue = (0, 0, 139)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
        pygame.draw.rect(screen, blue, [0, 0, 200, 600])
        pygame.draw.rect(screen, )
        pygame.display.update()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
'''

from edge import *
from graph import *
import sys

'''
g = Graph(6, False)
g.add_node(0)
g.add_node(3)
g.add_node(5)
s = g.show_matrix()
print(s)
print(g.show_list_of_nodes())
print(g.v())
print(g.has_node(5))
print(g.has_node(4))

g.del_node(0)
g.del_node(5)

print(g.show_matrix())
print(g.show_list_of_nodes())
#print(g.is_directed())

g.add_node(4)
g.add_node(1)
g.add_edge(edge(1, 3, 1))
g.add_edge(edge(4, 1, 1))
g.add_edge(edge(3, 4, 1))
print(g.show_matrix())
print(g.show_list_of_edges())
print(g.show_list_of_nodes())
print(g.e())




print(g.has_edge(edge(1,3,1)))
print(g.has_edge(edge(1,2,1)))

g.del_edge(edge(3,4,1))
g.del_edge(edge(1,3,1))
print(g.show_matrix())
'''



size = input("Wprowadz wielkosc grafu: ")
directed = input("Czy graf jest skierowany? (True lub False): ")

s = "Menu programu: \n"\
    + "1. Pokaz macierz sasiedztwa                2. Liczba wierzcholkow\n" \
    + "3. Liczba krawedzi                         4. Czy graf jest skierowany?\n"\
    + "5. Dodaj wierzcholek                       6. Czy wierzcholek znajduje sie w grafie?\n" \
    + "7. Usun wierzcholek                        8. Dodaj krawedz\n"\
    + "9. Czy krawedz znajduje sie w grafie?      10. Usun krawedz\n"

n = int(size)
d = bool(directed)

g = Graph(n, d)

while True:
    print(s)
    c = input("Wybierz opcje: ")
    match c:
        case "1":
            print(g.show_matrix())
        case "2":
            print("Liczba wierzcholkow: {} \n".format(g.v()))
        case "3":
            print("Liczba krawedzi: {} \n".format(g.e()))
            #print("Konczenie dzialania ...")
            #sys.exit()
        case "4":
            print("Skierowany? {} \n".format(g.is_directed()))
        case "5":
            n = int(input("Podaj numer wierzcholka ktory chcesz dodac [0, {}]: ".format(g.n-1)))
            g.add_node(n)
            print("Dodano wierzcholek o numerze: {} \n".format(n))
        case "6":
            n = int(input("Podaj numer wierzcholka: "))
            print(g.has_node(n))
            print("\n")
        case "7":
            n = int(input("Podaj numer wierzcholka ktory chcesz usunac [0, {}]: ".format(g.n-1)))
            g.del_node(n)
            print("Usunieto wierzcholek o numerze: {} \n".format(n))
        case "8":
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s, t, w)
            g.add_edge(ed)
            print("Dodano krawedz: ({}, {}, {})".format(s,t,w))
        case "9":
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s,t,w)
            print(g.has_edge(edge))
        case "10":
            s = int(input("Podaj od jakiego wierzcholka wychodzi krawedz: "))
            t = int(input("Podaj do jakiego wierzcholka wchodzi krawedz: "))
            w = int(input("Podaj wage krawedzi: "))
            ed = edge(s,t,w)
            g.del_edge(ed)
            print("Usunieto krawedz: ({}, {}, {})".format(s,t,w))
        case "21":
            print("Konczenie dzialania programu ...")
            sys.exit()