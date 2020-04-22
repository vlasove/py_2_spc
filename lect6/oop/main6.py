class Figure:
    color = "black"
    material = "paper"
    weight = 12

    def info(self):
        print(self.color, self.material, self.weight)

class Box:
    size = "LARGE"
    volume = "120 L"

    def info(self):
        print(self.size, self.volume)

class Circle(Box, Figure):

    def __init__(self, R):
        self.r = R 

    def print_circle(self):
        print("This is circle with r =", self.r)
        print('Length is:', self.r * 2 *3.1415)

        print("Figure info:",self.color, self.material, self.weight)

        
       # super().__init__()

c = Circle(10)
c.print_circle()
c.info()
