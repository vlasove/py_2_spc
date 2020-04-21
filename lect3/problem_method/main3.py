class Triangle:
    A = 0
    B = 0
    C = 0

    def perimeter(self):
        result = self.A + self.B + self.C 
        return result 

    def area(self):
        sp = (self.A + self.B + self.C) / 2  #semi perimeter
        result = sp * (sp - self.A) * (sp - self.B) * (sp - self.C)
        return result ** (0.5)

t = Triangle()
t.A = 1
t.B = 1
t.C = 1

print("Perimeter of ABC:", t.perimeter())
print("Area of ABC:", t.area())

