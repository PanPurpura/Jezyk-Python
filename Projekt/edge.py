class edge:
    """Klasa dla krawêdzi skierowanej z wag¹."""

    def __init__(self, source, target, weight=1):
        """Konstruktor krawêdzi."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentacjê napisow¹ krawêdzi."""
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))

    def __eq__(self, other):
        """Porównywanie krawêdzi (e1 == e2)."""
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        """Porównywanie krawêdzi (e1 != e2)."""
        return not self == other

    def __lt__(self, other):
        """Porównywanie krawêdzi (e1 < e2)."""
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __le__(self, other):
        """Porównywanie krawêdzi (e1 <= e2)."""
        return (self.weight, self.source, self.target) <= (
            other.weight, other.source, other.target)

    def __hash__(self):
        """Krawêdzie s¹ hashowalne."""
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Zwraca krawêdŸ o przeciwnym kierunku (~edge)."""
        return edge(self.target, self.source, self.weight)