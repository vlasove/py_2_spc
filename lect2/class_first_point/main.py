class Point:
    x = 0
    y = 0 

p1 = Point()

print(type(p1))
# a = []
# print(type(a))
print(p1.x, p1.y)
p1.x = 10
p1.y = 20
print("Current p1:",p1.x, p1.y)

p2 = Point()
p2.x = -10
p2.y = 30
print("Current p2:", p2.x, p2.y)


print(p1)
print(p2)