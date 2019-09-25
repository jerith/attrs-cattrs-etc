class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

Point(4, 5)

#########
# repr

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

Point(4, 5)
Point("four", 5)

#########
# validation

class Point:
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise ValueError("x must be an int")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

Point("four", 5)
Point(4, 5) == Point(5, 4)
Point(4, 5) == Point(4, 5)

#########
# validation by conversion

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

Point("four", 5)
Point(4, 5) == Point(5, 4)
Point(4, 5) == Point(4, 5)

#########
# comparison

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

Point(4, 5) == Point(5, 4)
Point(4, 5) == Point(4, 5)
p = Point(4, 5); p.x = 6; p

#########
# immutability

class Point:
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __init__(self, x, y):
        self._x = int(x)
        self._y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p = Point(4, 5); p.x = 6; p
