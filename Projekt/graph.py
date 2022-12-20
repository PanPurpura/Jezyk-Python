from multiprocessing import Value
from Projekt.edge import edge


class Graph:
    """Klasa dla grafu wa¿onego, skierowanego lub nieskierowanego."""

    matrix = [[]]
    list_of_nodes = []
    num_of_nodes = 0

    def __init__(self, n, directed=False):
        self.n = n                      # kompatybilnoœæ
        self.directed = directed        # bool, czy graf skierowany
        
        self.matrix = [[None for _ in range(self.n)] for _ in range(self.n)]

    def v(self):                       # zwraca liczbê wierzcho³ków
        num_of_ver = 0
        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] != None:
                    num_of_ver += 1
                    break

        return num_of_ver

    def e(self):                    # zwraca liczbê krawêdzi
        num_of_edg = 0
        if self.is_directed():
            for elem in range(len(self.matrix)):       #zliczanie krawedzi grafu skierowanego
                for elem1 in range(len(self.matrix[elem])):
                    if isinstance(self.matrix[elem][elem1], edge()):
                        num_of_edg += 1
        else:                       # zliczanie krawedzi grafu nieskierowanego
            i = 0
            j = 0
            for elem in range(len(self.matrix)):
                while(j <= i and i < len(self.matrix[elem])):
                    if isinstance(self.matrix[elem][j], edge()):
                        num_of_edg += 1
                        j += 1
                i += 1
                j = 0

        return num_of_edg


    def is_directed(self):              # bool, czy graf skierowany
        return self.directed

    def add_node(self, node):       # dodaje wierzcho³ek
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))

        for i in range(self.n):
            self.matrix[node][i] = 0

        self.num_of_nodes += 1
        self.list_of_nodes.append(node)


    def has_node(self, node):      # bool
        if node > self.n-1 or node < 0:
            raise ValueError("W grafie znajduja sie jedynie dodane wierzcholki w zakresie [0, {}]".format(self.n-1))

        if node in self.list_of_nodes:
            return True
        else:
            return False

    def del_node(self, node):       # usuwa wierzcho³ek
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna usunac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))

        for i in range(self.n):
            self.matrix[node][i] = None

        for elem in self.list_of_nodes:
            if elem == node:
                self.list_of_nodes.remove(elem)

    def add_edge(self, edge):       # wstawienie krawêdzi
        if not self.is_directed(): # dodanie krawedzi do grafu nieskierowanego
            if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edge.source][edge.target] = edge
            self.matrix[edge.target][edge.source] = edge
        else:
            if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edge.source][edge.target] = edge

    def has_edge(self, edge):
        return isinstance(self.matrix[edge.source][edge.target], edge)

    def del_edge(self, edge):     # usuniêcie krawêdzi

        if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

        if self.is_directed():
            self.matrix[edge.source][edge.target] = None
        else:
            self.matrix[edge.source][edge.target] = None
            self.matrix[edge.target][edge.source] = None

    def weight(self, edge):        # zwraca wagê krawêdzi
        if not self.has_edge():
            raise ValueError("Graf nie ma takiej krawedzie!")

        return edge.weight

    def iternodes(self):         # iterator po wierzcho³kach
        iternodes = IterNode()
        iternodes_iter = iter(iternodes)

        return iternodes_iter

    def iteradjacent(self, node):  # iterator po wierzcho³kach s¹siednich
        neighbour = []
        for elem in self.matrix[node]:
            if isinstance(self.matrix[node][elem], edge):
                neighbour.append(self.matrix[node][elem].target)

        iteradjacent = IterAdjacent(neighbour)
        iteradjacent_iter = iter(iteradjacent)

        return iteradjacent_iter

    def iteroutedges(self, node): pass  # iterator po krawêdziach wychodz¹cych

    def iterinedges(self, node): pass   # iterator po krawêdziach przychodz¹cych

    def iteredges(self): pass           # iterator po krawêdziach

    def copy(self):                # zwraca kopiê grafu
        new_graph = Graph(self.n, self.directed)

        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                new_graph.matrix[elem][elem1] = self.matrix[elem][elem1]

        new_graph.list_of_nodes = self.list_of_nodes

        for elem in self.list_of_nodes:
            new_graph.add_node(self.list_of_nodes[elem])

        return new_graph

    def transpose(self):           # zwraca graf transponowany]
        if self.is_directed():
            return self
        else:
            new_graph = Graph(self.n, self.directed)
            new_graph.list_of_nodes = self.list_of_nodes

            for elem in self.list_of_nodes:
                new_graph.add_node(self.list_of_nodes[elem])

            i = 0
            j = 0
            for elem in range(len(self.matrix)):
                while(j <= i and i < len(self.matrix[elem])):
                    new_graph.matrix[elem][j] = self.matrix[j][elem]
                    new_graph.matrix[j][elem] = self.matrix[elem][j]
                    j += 1
                i += 1
                j = 0
            
            return  new_graph
                

    def complement(self):         # zwraca dope³nienie grafu
        new_graph = Graph(self.n, self.directed)
        new_graph.list_of_nodes = self.list_of_nodes
        
        for elem in self.list_of_nodes:
            new_graph.add_node(self.list_of_nodes[elem])

        for elem in new_graph.list_of_nodes:
            for elem1 in range(len(self.matrix[elem])):
                if isinstance(self.matrix[elem][elem1], edge):
                    continue
                else:
                    new_graph.add_edge(edge(elem, elem1))

    def subgraph(self, nodes): pass     # zwraca podgraf indukowany

class IterNode:
    def __iter__(self):
        self.node = Graph.list_of_nodes[0]
        return self

    def __next__(self):
        i = 1
        if i < len(Graph.list_of_nodes):
            next_node = self.node
            self.node = Graph.list_of_nodes[i]
            i += 1
            return self.node
        else:
            raise StopIteration

class IterAdjacent:
    def __iter__(self, neigh):
        self.neigh = neigh
        self.res = neigh[0]
        return self

    def __next__(self):
        i = 1
        if i < len(self.neigh):
            next_res = self.res
            self.res = self.neigh[i]
            i += 1
            return self.res
        else:
            raise StopIteration