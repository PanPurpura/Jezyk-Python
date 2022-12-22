from multiprocessing import Value
from edge import edge


class Graph:
    """Klasa dla grafu wazonego, skierowanego lub nieskierowanego."""

    matrix = [[]]
    list_of_nodes = []
    list_of_edges = []
    num_of_nodes = 0

    def __init__(self, n, directed=False):
        self.n = n                      # kompatybilnosc
        self.directed = directed        # bool, czy graf skierowany
        
        self.matrix = [[None for _ in range(self.n)] for _ in range(self.n)]

    def v(self):    # zwraca liczbe wierzcholkow                                                                                    SUCCESS
        return len(self.list_of_nodes)

    def e(self):                    # zwraca liczbe krawedzi
        if not self.is_directed():
            return len(self.list_of_edges)//2

        return len(self.list_of_edges)


    def is_directed(self):              # bool, czy graf skierowany                                                                 SUCCESS
        return self.directed

    def add_node(self, node):       # dodaje wierzcholek                                                                            SUCCESS
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))
        if node in self.list_of_nodes:
            raise ValueError("Wierzcholek jest juz dodany!")

        for i in range(self.n):
            self.matrix[node][i] = 0

        self.num_of_nodes += 1
        self.list_of_nodes.append(node)


    def has_node(self, node):      # bool                                                                                           SUCCESS
        if node > self.n-1 or node < 0:
            raise ValueError("W grafie znajduja sie jedynie dodane wierzcholki w zakresie [0, {}]".format(self.n-1))

        if node in self.list_of_nodes:
            return True
        else:
            return False

    def del_node(self, node):       # usuwa wierzcholek                                                                             SUCCESS
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna usunac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))

        for i in range(self.n):
            self.matrix[node][i] = None

        for elem in self.list_of_nodes:
            if elem == node:
                self.list_of_nodes.remove(elem)
                break

    def add_edge(self, edge):       # wstawienie krawedzi
        if not (edge.source in self.list_of_nodes or edge.target in self.list_of_nodes):
            raise ValueError("Probujesz dodac krawedz do wierzcholka lub od wierzcholka ktory nie istnieje!")
        
        if not self.is_directed(): # dodanie krawedzi do grafu nieskierowanego
            if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edge.source][edge.target] = edge
            self.list_of_edges.append(edge)

            ed = edge.__invert__()
            self.matrix[edge.target][edge.source] = ed
            self.list_of_edges.append(ed)
        else:
            if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edge.source][edge.target] = edge
            self.list_of_edges.append(edge)

    def has_edge(self, edge):
        return isinstance(self.matrix[edge.source][edge.target], edge)
        #return edge in self.list_of_edges

    def del_edge(self, edge):     # usuniecie krawedzi

        if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")
        elif not edge in self.list_of_edges:
            raise ValueError("Nie ma takiej krawedzi w grafie!")

        if self.is_directed():
            self.matrix[edge.source][edge.target] = 0

            for elem in self.list_of_edges:
                if elem.source == edge.source and elem.target == edge.target and elem.weight == edge.weight:
                    self.list_of_edges.remove(elem)
                    break
        else:
            self.matrix[edge.source][edge.target] = 0
            self.matrix[edge.target][edge.source] = 0

            for elem in self.list_of_edges:
                if (elem.source == edge.source and elem.target == edge.target and elem.weight == edge.weight) or (elem.source == edge.target and elem.target == edge.source and elem.weight == edge.weight):
                    self.list_of_edges.remove(elem)
                    break

    def neighbours(self, node):
        l = []
        if node in self.list_of_nodes:
            for elem in range(len(self.matrix[node])):
                if isinstance(self.matrix[node][elem], edge):
                    l.append(self.matrix[node][elem].target)

        return l

    def weight(self, edge):        # zwraca wage krawedzi
        if not self.has_edge():
            raise ValueError("Graf nie ma takiej krawedzi!")

        return edge.weight

    def iternodes(self):         # iterator po wierzcholkach
        iternodes = IterNode()
        iternodes_iter = iter(iternodes)

        return iternodes_iter

    def iteradjacent(self, node):  # iterator po wierzcholkach sasiednich
        neigh = self.neighbours(node)

        iteradjacent = IterAdjacent(neigh)
        iteradjacent_iter = iter(iteradjacent)

        return iteradjacent_iter

    def iteroutedges(self, node):  # iterator po krawedziach wychodzacych
        
        l = [] 
        for elem in self.matrix[node]:
            if isinstance(self.matrix[node][elem], edge):
                l.append(self.matrix[node][elem])

        iterout = IterOutEdges(l)
        iterout_it = iter(iterout)

        return iterout_it

    def iterinedges(self, node):   # iterator po krawedziach przychodzacych
        l = [] 
        for elem in self.matrix[node]:
            if isinstance(self.matrix[elem][node], edge):
                l.append(self.matrix[elem][node])

        inner = IterInEdges(l)
        inner_iter = iter(inner)

        return inner_iter

    def iteredges(self):           # iterator po krawedziach
        iteredg = IterEdges()
        iteredg_iter = iter(iteredg)

        return iteredg_iter

    def copy(self):                # zwraca kopie grafu
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
                

    def complement(self):         # zwraca dopelnienie grafu
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

    def subgraph(self, nodes):     # zwraca podgraf indukowany
        new_graph = Graph(self.n, self.directed)
        new_graph.list_of_nodes = self.list_of_nodes

        for elem in nodes:
            new_graph.add_node(self.list_of_nodes[elem])

        for elem in nodes:
            for elem1 in self.matrix[elem]:
                if self.matrix[elem][elem1].target in nodes:
                    new_graph.matrix[elem][elem1] = self.matrix[elem][elem1]
                else:
                    continue

        return new_graph

    def show_matrix(self):
        s = ""
        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                if isinstance(self.matrix[elem][elem1], edge):
                    s += " e"
                elif self.matrix[elem][elem1] == 0:
                    s += " 0"
                else:
                    s += " n"
            s += "\n"

        return s

    def show_list_of_nodes(self):
        s = ""
        for elem in range(len(self.list_of_nodes)):
            s += "{}, ".format(self.list_of_nodes[elem])

        return s

    def show_list_of_edges(self):
        s = ""
        for elem in range(len(self.list_of_edges)):
            s += "({}, {}, {}) ".format(self.list_of_edges[elem].source, self.list_of_edges[elem].target, self.list_of_edges[elem].weight)

        return s
                    
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

class IterEdges:
    def __iter__(self, neigh):
        self.edges = Graph.list_of_edges[0]
        return self

    def __next__(self):
        i = 1
        if i < len(Graph.list_of_edges):
            next_edge = self.edges
            self.edges = Graph.list_of_edges[i]
            i += 1
            return self.edges
        else:
            raise StopIteration

class IterOutEdges:
    def __iter__(self, out):
        self.o = out
        self.res = self.o[0]
        return self

    def __next__(self):
        i = 1
        if i < len(self.o):
            next_edge = self.res
            self.res = self.o[i]
            i += 1
            return self.res
        else:
            raise StopIteration

class IterInEdges:
    def __iter__(self, inner):
        self.li = inner
        self.res = self.li[0]
        return self

    def __next__(self):
        i = 1
        if i < len(self.li):
            next_edge = self.res
            self.res = self.li[i]
            i += 1
            return self.res
        else:
            raise StopIteration