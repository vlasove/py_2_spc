class Point:
    x = 0
    y = 0 


def distance(point1, point2):
    dx = point1.x - point2.x 
    dy = point1.y - point2.y 
    return  (dx**2 + dy**2) ** (0.5)


p1 = Point()
p1.x = 10
p1.y = 30

p2 = Point()
p2.x = 1000
p2.y = 9391

print("Calc distance:", distance(p1, p2))
