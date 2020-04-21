class Triangle:
    A = 0
    B = 0
    C = 0

    def perimeter(self):
        result = self.A + self.B + self.C
        return result 

    def area(self):
        sp =  self.perimeter() / 2  #semi perimeter
        result = sp * (sp - self.A) * (sp - self.B) * (sp - self.C)
        return result ** (0.5)


t = Triangle()
print(t.area())