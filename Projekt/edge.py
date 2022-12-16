class edge:
    """Klasa dla kraw�dzi skierowanej z wag�."""

    def __init__(self, source, target, weight=1):
        """Konstruktor kraw�dzi."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentacj� napisow� kraw�dzi."""
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))

    def __eq__(self, other):
        """Por�wnywanie kraw�dzi (e1 == e2)."""
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        """Por�wnywanie kraw�dzi (e1 != e2)."""
        return not self == other

    def __lt__(self, other):
        """Por�wnywanie kraw�dzi (e1 < e2)."""
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __le__(self, other):
        """Por�wnywanie kraw�dzi (e1 <= e2)."""
        return (self.weight, self.source, self.target) <= (
            other.weight, other.source, other.target)

    def __hash__(self):
        """Kraw�dzie s� hashowalne."""
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Zwraca kraw�d� o przeciwnym kierunku (~edge)."""
        return edge(self.target, self.source, self.weight)