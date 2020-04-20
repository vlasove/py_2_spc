class Point:
    x = 0
    y = 0 

def distance(point1, point2):
    dx = point1.x - point2.x 
    dy = point1.y - point2.y 
    return  (dx**2 + dy**2) ** (0.5)

def points_creator(X,Y):
    p1 = Point()
    p1.x = X
    p1.y = Y
    return p1 

my_point = points_creator(2,4)
print("Coordinates of this point:", my_point.x, my_point.y)
print(type(my_point))


