class Figure:
    color = "black"
    material = "paper"
    weight = 12

class Box:
    size = "LARGE"
    volume = "120 L"

class Circle(Figure, Box):

    def __init__(self, R):
        self.r = R 

    def print_circle(self):
        print("This is circle with r =", self.r)
        print('Length is:', self.r * 2 *3.1415)

        print("Figure info:",self.color, self.material, self.weight)

        print("Box info:", self.size, self.volume)

c = Circle(10)
c.print_circle()
