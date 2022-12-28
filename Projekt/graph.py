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
        self.list_of_nodes = []
        self.list_of_edges = []

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

        new_list = []
        for elem in self.list_of_edges:
            if elem.source == node or elem.target == node:
                self.matrix[elem.source][elem.target] = 0
            else:
                new_list.append(elem)

        self.list_of_edges = new_list

        for i in range(self.n):
            self.matrix[node][i] = None

        for elem in self.list_of_nodes:
            if elem == node:
                self.list_of_nodes.remove(elem)
                break

    def add_edge(self, edg):       # wstawienie krawedzi
        if not (edg.source in self.list_of_nodes and edg.target in self.list_of_nodes):
            raise ValueError("Probujesz dodac krawedz do wierzcholka lub od wierzcholka ktory nie istnieje!")
        if edg in self.list_of_edges:
            raise ValueError("Krawedz juz istnieje!")
        
        if self.is_directed() == False: # dodanie krawedzi do grafu nieskierowanego
            if edg.source > self.n-1 or edg.source < 0 or edg.target > self.n-1 or edg.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edg.source][edg.target] = edg
            self.list_of_edges.append(edg)

            ed = edge(edg.target, edg.source, edg.weight)
            self.matrix[edg.target][edg.source] = ed
            self.list_of_edges.append(ed)
        else:
            if edg.source > self.n-1 or edg.source < 0 or edg.target > self.n-1 or edg.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edg.source][edg.target] = edg
            self.list_of_edges.append(edg)

    def has_edge(self, edge):
        return edge in self.list_of_edges

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

    def weight(self, edge_s, edge_t):        # zwraca wage krawedzi
        return self.matrix[edge_s][edge_t].weight

    def iternodes(self):         # iterator po wierzcholkach

       return iter(self.list_of_nodes)

    def iteradjacent(self, node):  # iterator po wierzcholkach sasiednich
        neigh = self.neighbours(node)

        return iter(neigh)

    def iteroutedges(self, node):  # iterator po krawedziach wychodzacych
        
        l = [] 
        for elem in self.matrix[node]:
            if isinstance(elem, edge):
                l.append(elem)

        return iter(l)

    def iterinedges(self, node):   # iterator po krawedziach przychodzacych
        l = [] 
        for elem in self.list_of_edges:
            if elem.target == node:
                l.append(elem)

        return iter(l)

    def iteredges(self):           # iterator po krawedziach
        return iter(self.list_of_edges)

    def copy(self):                # zwraca kopie grafu
        new_graph = Graph(self.n, self.directed)

        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                new_graph.matrix[elem][elem1] = self.matrix[elem][elem1]

        new_graph.list_of_nodes = self.list_of_nodes 
        new_graph.list_of_edges = self.list_of_edges
       
        return new_graph

    def transpose(self):           # zwraca graf transponowany]
        if not self.is_directed():
            return self
        else:
            new_graph = Graph(self.n, self.directed)

            for elem in self.list_of_nodes:
                new_graph.add_node(elem)

            for elem in self.list_of_edges:
                new_graph.add_edge(elem.__invert__())
         
            return  new_graph
                

    def complement(self):         # zwraca dopelnienie grafu
        new_graph = Graph(self.n, self.directed)
        
        for elem in self.list_of_nodes:
            new_graph.add_node(elem)

        for elem in new_graph.list_of_nodes:
            for elem1 in range(len(self.matrix[elem])):
                if isinstance(self.matrix[elem][elem1], edge):
                    continue
                else:
                    try:
                        new_graph.add_edge(edge(elem, elem1))
                    except ValueError:
                        continue

        return new_graph

    def subgraph(self, nodes):     # zwraca podgraf indukowany

        for elem in nodes:
            if not elem in self.list_of_nodes:
                raise ValueError("Wyjsciowy graf nie ma jednego lub wielu z podanych wierzcholkow")

        new_graph = Graph(self.n, self.directed)

        for elem in nodes:
            new_graph.add_node(elem)

        for elem in nodes:
            for elem1 in range(len(self.matrix[elem])):
                if isinstance(self.matrix[elem][elem1], edge):
                    if self.matrix[elem][elem1].target in nodes:
                        try:
                            new_graph.add_edge(edge(elem, elem1, self.matrix[elem][elem1].weight))
                        except ValueError:
                            continue

                    else:
                        continue
                else:
                    continue

        return new_graph

    def show_matrix(self):
        s = "Macierz sasiedztwa: \n\n   "
        for i in range(0, self.n):
            s += "{} ".format(i)
        s+="\n"

        for elem in range(len(self.matrix)):
            s += "{} ".format(elem)
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