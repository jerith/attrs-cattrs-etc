import attr

@attr.s
class Point:
    x = attr.ib()
    y = attr.ib()

Point(4, 5)
Point("four", 5)

#########
# validation

from attr import validators as av

@attr.s
class Point:
    x = attr.ib()
    y = attr.ib(validator=av.instance_of(int))

    @x.validator
    def _validate_y(self, attribute, value):
        if not isinstance(value, int):
            raise ValueError("x must be an int")

#########
# validation by conversion

@attr.s
class Point:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

Point("four", 5)
Point(4, 5) == Point(5, 4)
Point(4, 5) == Point(4, 5)

#########
# turn off comparison

@attr.s(cmp=False)
class Point:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

Point(4, 5) == Point(5, 4)
Point(4, 5) == Point(4, 5)
p = Point(4, 5); p.x = 6; p

#########
# immutability

@attr.s(frozen=True)
class Point:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

p = Point(4, 5); p.x = 6; p
