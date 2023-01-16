from multiprocessing import Value
from edge import Edge


class Graph:
    """Klasa dla grafu wazonego, skierowanego lub nieskierowanego."""

    def __init__(self, n, directed=False):
        self.n = n                      # kompatybilnosc
        self.directed = directed        # bool, czy graf skierowany
        
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def v(self):    # zwraca liczbe wierzcholkow                                                                                    SUCCESS
        return self.n

    def e(self):                    # zwraca liczbe krawedzi
        num_of_edges = 0
        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] != 0:
                    num_of_edges += 1

        if self.is_directed() == False:
            return num_of_edges//2

        return num_of_edges


    def is_directed(self):              # bool, czy graf skierowany                                                                 SUCCESS
        return self.directed

   # def add_node(self, node):       # dodaje wierzcholek                                                                            SUCCESS
    #    if node > self.n-1 or node < 0:
     #       raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))
      #  if node in self.list_of_nodes:
       #     raise ValueError("Wierzcholek jest juz dodany!")

        #for i in range(self.n):
         #   self.matrix[node][i] = 0

       # self.num_of_nodes += 1
       # self.list_of_nodes.append(node)


    def has_node(self, node):      # bool                                                                                           SUCCESS
        if node > self.n-1 or node < 0:
            raise ValueError("W grafie znajduja sie jedynie dodane wierzcholki w zakresie [0, {}]".format(self.n-1))

        if node in range(0, self.n):
            return True
        else:
            return False

    def del_node(self, node):       # usuwa wierzcholek                                                                             SUCCESS
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna usunac jedynie wierzcholki w zakresie [0, {}]".format(self.n-1))

        for elem in range(len(self.matrix[node])):
            self.matrix[node][elem] = 0
            self.matrix[elem][node] = 0

    def add_edge(self, edg):       # wstawienie krawedzi
        if not (edg.source in range(0, self.n) and edg.target in range(0, self.n)):
            raise ValueError("Probujesz dodac krawedz do wierzcholka lub od wierzcholka ktory nie istnieje!")
        if self.matrix[edg.source][edg.target] != 0:
            raise ValueError("Krawedz juz istnieje!")
        
        if self.is_directed() == False: # dodanie krawedzi do grafu nieskierowanego
            if edg.source > self.n-1 or edg.source < 0 or edg.target > self.n-1 or edg.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edg.source][edg.target] = edg.weight

            ed = ~edg
            self.matrix[edg.target][edg.source] = ed.weight
        else:
            if edg.source > self.n-1 or edg.source < 0 or edg.target > self.n-1 or edg.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")

            self.matrix[edg.source][edg.target] = edg.weight

    def has_edge(self, edge):
        return self.matrix[edge.source][edge.target] != 0

    def del_edge(self, edge):     # usuniecie krawedzi
        if edge.source > self.n-1 or edge.source < 0 or edge.target > self.n-1 or edge.target < 0:
                raise ValueError("Krawedz ma bledne wierzcholki!")
        elif not self.matrix[edge.source][edge.target] == 1:
            raise ValueError("Nie ma takiej krawedzi w grafie!")

        if self.is_directed():
            self.matrix[edge.source][edge.target] = 0

        else:
            self.matrix[edge.source][edge.target] = 0
            self.matrix[edge.target][edge.source] = 0

    def neighbours(self, node):
        l = []
        if node in range(0, self.n-1):
            for elem in range(len(self.matrix[node])):
                if self.matrix[node][elem] != 0:
                    l.append(elem)

        return l

    def weight(self, edge):        # zwraca wage krawedzi
        return self.matrix[edge.source][edge.target]

    def iternodes(self):         # iterator po wierzcholkach
       l = []
       for i in range(0, self.n):
           l.append(i)

       return iter(l)

    def iteradjacent(self, node):  # iterator po wierzcholkach sasiednich
        neigh = self.neighbours(node)

        return iter(neigh)

    def iteroutedges(self, node):  # iterator po krawedziach wychodzacych
        
        l = [] 
        for elem in range(len(self.matrix[node])):
            if self.matrix[node][elem] != 0:
                edg = Edge(node, elem, self.matrix[node][elem])
                l.append(edg)

        return iter(l)

    def iterinedges(self, node):   # iterator po krawedziach przychodzacych
        l = [] 
        for elem in range(len(self.matrix[node])):
            if self.matrix[elem][node] != 0:
                edg = Edge(elem, node, self.matrix[elem][node])
                l.append(edg)

        return iter(l)

    def iteredges(self):           # iterator po krawedziach
        l = []

        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] != 0:
                    edg = Edge(elem, elem1, self.matrix[elem][elem1])
                    l.append(edg)

        return iter(l)


    def copy(self):                # zwraca kopie grafu
        new_graph = Graph(self.n, self.directed)

        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                new_graph.matrix[elem][elem1] = self.matrix[elem][elem1]
       
        return new_graph

    def transpose(self):           # zwraca graf transponowany]
        if not self.is_directed():
            return self
        else:
            new_graph = Graph(self.n, self.directed)

            for elem in range(len(self.matrix)):
                for elem1 in range(len(self.matrix[elem])):
                    if self.matrix[elem][elem1] != 0:
                        new_graph.matrix[elem1][elem] = self.matrix[elem][elem1]
         
            return  new_graph
                

    def complement(self):         # zwraca dopelnienie grafu
        new_graph = Graph(self.n, self.directed)

        for elem in range(len(self.matrix)):
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] == 0:
                    new_graph.matrix[elem][elem1] = 1
                else:
                    continue

        return new_graph

    def subgraph(self, nodes):     # zwraca podgraf indukowany

        for elem in range(len(nodes)):
            if not elem in range(0, self.n):
                raise ValueError("Wyjsciowy graf nie ma jednego lub wielu z podanych wierzcholkow")

        new_graph = Graph(self.n, self.directed)

        for elem in nodes:
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] != 0 and (elem1 in nodes) == True:
                    new_graph.matrix[elem][elem1] = self.matrix[elem][elem1]

        return new_graph

    def show_matrix(self):
        s = "Macierz sasiedztwa: \n\n   "
        for i in range(0, self.n):
            s += "{} ".format(i)
        s+="\n"

        for elem in range(len(self.matrix)):
            s += "{} ".format(elem)
            for elem1 in range(len(self.matrix[elem])):
                if self.matrix[elem][elem1] == 0:
                    s += " 0"
                else:
                    s += " {}".format(self.matrix[elem][elem1])
            s += "\n"

        return s

    def DFS(self, node, vis):
        if node not in vis:
            vis.append(node)
            for neighbour in self.neighbours(node):
                self.DFS(neighbour, vis)

    def BFS(self, node, vis, queue):
        vis.append(node)
        queue.append(node)

        while queue:
            m = queue.pop(0)
            for neighbour in self.neighbours(m):
                if neighbour not in vis:
                    vis.append(neighbour)
                    queue.append(neighbour)