class Circle:
    def __init__(self, R):
        self.r = R 

    def perimenter(self):
        print("Length of Cirlce is:", self.r * 2 * 3.1415) 

class Rectangle:
    def __init__(self, A,B):
        self.a = A 
        self.b = B  

    def perimenter(self):
        print("Per of rectangle is:", 2*(self.a + self.b))

class Triangle:
    def __init__(self, A,B,C):
        self.a = A 
        self.b = B 
        self.c = C 

    def perimenter(self):
        print("Per of triangle:", self.a + self.b +self.c)

c = Circle(20)
r = Rectangle(10,20)
t = Triangle(1,2,3)

figures = [c,t,r]
for fig in figures:
    fig.perimenter()