from collections import namedtuple

# class Point:
#     x = 0
#     y = 0 

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)
print(p[0], p[1])
print(p)
print(Point)

