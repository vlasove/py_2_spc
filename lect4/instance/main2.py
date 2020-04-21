class Point:
    def __init__(self, X = 0, Y = 0):
        self.x = X 
        self.y = Y 

    def __str__(self):
        return "X:{} Y:{}".format(self.x, self.y)

    # def __repr__(self):
    #     return "<Point X:{} Y:{}>".format(self.x, self.y)

p1 = Point(1,2)
p2 = Point(3,4)

q = [p1, p2]
print(p1)