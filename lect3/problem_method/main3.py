class Triangle:
    A = 0
    B = 0
    C = 0

    def perimeter(self):
        result = self.A + self.B + self.C 
        return result 

    def area(self):
        pass 

t = Triangle()
t.A = 3
t.B = 3
t.C = 3 

print("Perimeter of ABC:", t.perimeter())
print("Area of ABC:", t.area())

