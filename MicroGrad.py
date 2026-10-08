class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self._prev = set(_children)

    def __repr__(self):
        return f"data: {self.data}"
    def __add__(self, other):
        return Value(self.data + other.data, (self, other))
    def __sub__(self, other):
        return Value(self.data - other.data, (self, other))
    def __mul__(self, other):
        return Value(self.data * other.data, (self, other))


a = Value(2)
b = Value(-3)

d = a + b
c = Value(-5)
e = d * c
f = Value(2)
g = e * f
print(g._prev)
def Propogate(val, target):
    ancestors = val._prev
    found = False
    for ancestor in ancestors:
        branch = []
        branch.append(ancestor)
        exploring = ancestor

        while exploring != target:
            secondary_ancestors = exploring._prev
            if secondary_ancestors:
                for ancestort in secondary_ancestors:
                    exploring = ancestort


            else:
                break
        return exploring,found










print(Propogate(g, a))