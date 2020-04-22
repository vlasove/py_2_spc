class Circle:
    def __init__(self, R):
        self.__r = R 

    def perimenter(self):
        print("Length of Cirlce is:", self.__r * 2 * 3.1415) 

class Rectangle:
    def __init__(self, A,B):
        self.__a = A 
        self.__b = B  

    def perimenter(self):
        print("Per of rectangle is:", 2*(self.__a + self.__b))

class Triangle:
    def __init__(self, A,B,C):
        self.__a = A 
        self.__b = B 
        self.__c = C 

    def perimenter(self):
        print("Per of triangle:", self.__a + self.__b +self.__c)

c = Circle(20)
r = Rectangle(10,20)
t = Triangle(1,2,3)

figures = [c,t,r]
for fig in figures:
    fig.perimenter()