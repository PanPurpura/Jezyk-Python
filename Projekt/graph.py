from Projekt.edge import edge


class Graph:
    """Klasa dla grafu wa�onego, skierowanego lub nieskierowanego."""

    matrix = [[]]
    list_of_nodes = []
    num_of_nodes = 0

    def __init__(self, n, directed=False):
        self.n = n                      # kompatybilno��
        self.directed = directed        # bool, czy graf skierowany
        
        self.matrix = [[None for _ in range(self.n)] for _ in range(self.n)]

    def v(self):                       # zwraca liczb� wierzcho�k�w
        num_of_ver = 0
        for elem in len(self.matrix):
            for elem1 in len(self.matrix[elem]):
                if self.matrix[elem][elem1] != None:
                    num_of_ver += 1
                    break

        return num_of_ver

    def e(self):                    # zwraca liczb� kraw�dzi
        num_of_edg = 0
        for elem in len(self.matrix):
            for elem1 in len(self.matrix[elem]):
                if isinstance(self.matrix[elem][elem1], edge()):
                    num_of_edg += 1

        return num_of_edg


    def is_directed(self):              # bool, czy graf skierowany
        return self.directed

    def add_node(self, node):       # dodaje wierzcho�ek
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n))

        for i in range(self.n):
            self.matrix[node][i] = 0

        self.num_of_nodes += 1
        self.list_of_nodes.append(node)


    def has_node(self, node):      # bool
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n))

        if node in self.list_of_nodes:
            return True
        else:
            return False

    def del_node(self, node):       # usuwa wierzcho�ek
        if node > self.n-1 or node < 0:
            raise ValueError("Mozna dodac jedynie wierzcholki w zakresie [0, {}]".format(self.n))

        for i in range(self.n):
            self.matrix[node][i] = None

    def add_edge(self, edge):       # wstawienie kraw�dzi
        if edge.source > self.n or edge.source < 0 or edge.target > self.n or edge.target < 0:
            raise ValueError("Krawedz ma bledne wierzcholki!")

        self.matrix[edge.source][edge.target] = edge
        self.matrix[edge.target][edge.source] = edge

    def has_edge(self, edge): pass      # bool

    def del_edge(self, edge): pass      # usuni�cie kraw�dzi

    def weight(self, edge): pass        # zwraca wag� kraw�dzi

    def iternodes(self): pass           # iterator po wierzcho�kach

    def iteradjacent(self, node): pass  # iterator po wierzcho�kach s�siednich

    def iteroutedges(self, node): pass  # iterator po kraw�dziach wychodz�cych

    def iterinedges(self, node): pass   # iterator po kraw�dziach przychodz�cych

    def iteredges(self): pass           # iterator po kraw�dziach

    def copy(self): pass                # zwraca kopi� grafu

    def transpose(self): pass           # zwraca graf transponowany

    def complement(self): pass          # zwraca dope�nienie grafu

    def subgraph(self, nodes): pass     # zwraca podgraf indukowany

