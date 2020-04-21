class Point:
    def __init__(self, X = 0, Y = 0):
        self.x = X 
        self.y = Y 

    def show(self):
        print("X:", self.x, "Y:", self.y)

p1 = Point(1,2)

print(type(p1))
print(isinstance(p1, Point))
print(isinstance(p1, int))
print(isinstance(p1, dict))