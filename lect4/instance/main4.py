class Point:
    def __init__(self, X = 0, Y = 0):
        print("Point created", X,Y)
        self.x = X 
        self.y = Y 

    def __del__(self):
        print("THIS OBJECT DELETED!", self.x, self.y)

p = Point(1,2)
p1 = Point(2,2)

# del p1 

print(p)
del p 
print(p)























































del p
del p1