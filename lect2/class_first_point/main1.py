class Point:
    x = 0
    y = 0 

p1 = Point()
p1.x = 1
p1.y = 1


p2 = Point()
p2.x = 3
p2.y = 3


dx = p1.x - p2.x 
dy = p1.y - p2.y 

distance = (dx**2 + dy**2) ** (0.5)
print(distance)