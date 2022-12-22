class edge:
    """Klasa dla krawedzi skierowanej z waga."""

    def __init__(self, source, target, weight=1):
        """Konstruktor krawedzi."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentacje napisowa krawedzi."""
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))

    def __eq__(self, other):
        """Porownywanie krawedzi (e1 == e2)."""
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        """Porownywanie krawedzi (e1 != e2)."""
        return not self == other

    def __lt__(self, other):
        """Porownywanie krawedzi (e1 < e2)."""
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __le__(self, other):
        """Porownywanie krawedzi (e1 <= e2)."""
        return (self.weight, self.source, self.target) <= (
            other.weight, other.source, other.target)

    def __hash__(self):
        """Krawedzie sa hashowalne."""
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Zwraca krawedz o przeciwnym kierunku (~edge)."""
        return edge(self.target, self.source, self.weight)