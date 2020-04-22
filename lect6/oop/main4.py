# Наследование - свойство объектов, перенимать состояние родительских объектов (родительских классов),а также
# дополнять их и изменять. 

class Figure:
    color = "black"
    material = "paper"
    weight = 12

class Circle(Figure):
    def __init__(self, R):
        self.r = R 

    def print_circle(self):
        print("#######################CIRCLE#################")
        print("This is", self.color, "circle")
        print("Material:", self.material)
        print("Length of circle:", self.r * 3.1415 * 2)

class Triangle(Figure):
    def __init__(self, A,B,C):
        self.a = A 
        self.b = B 
        self.c = C 
    
    def print_triangle(self):
        print("#################TRIANGLE##############")
        print("This is", self.color, "triangle")
        print("Material:", self.material)
        print("Perimeter of triangle:", self.a + self.b + self.c)


class PifagorTriangle(Triangle):
    def print_triangle(self):
        print("PIFAGOREAN TRIANGLE") 

t = Triangle(3,4,5)
t.print_triangle()
c = Circle(10)
c.print_circle()
pf = PifagorTriangle(6,8,10)
pf.print_triangle()




