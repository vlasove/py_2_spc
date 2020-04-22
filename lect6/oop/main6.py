class Figure:
    color = "black"
    material = "paper"
    weight = 12

    def __info(self):
        print(self.color, self.material, self.weight)

class Box:
    size = "LARGE"
    volume = "120 L"

    def __info(self):
        print(self.size, self.volume)

class Circle(Box, Figure):

    def __init__(self, R):
        self.r = R 

    def print_circle(self):
        print("This is circle with r =", self.r)
        print('Length is:', self.r * 2 *3.1415)

        self._Box__info()
        Figure._Figure__info(self)
        
        print("Figure info:",self.color, self.material, self.weight)

        
       

c = Circle(10)
c.print_circle()

