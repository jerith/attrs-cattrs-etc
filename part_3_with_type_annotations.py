import attr

@attr.s(auto_attribs=True)
class Point:
    x: int
    y: int

Point(4, 5)
Point("four", 5)
