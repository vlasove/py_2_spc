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

p3 = Point()
p3.x = 200
p3.y = 4300

points = [p1,p2,p3]
distances = [distance(p1,p2),distance(p2,p3),distance(p1,p3)]
hypotenuse = max(distances)
distances.remove(hypotenuse)

if hypotenuse ** 2 == (distances[0] ** 2 + distances[1] ** 2):
    print("TRUE")
else:
    print("FALSE")