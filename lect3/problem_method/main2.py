class Figure:
    #Переменная класса - поле класса - атрибут (класса)
    a = 0 
    b = 0

    #Метод класса - (метод) - функция, опеределенная внутри класса
    def perimeter(self):
        return 2*(self.a + self.b)

    def area(self):
        return self.a * self.b 

def figure_creator(A,B):
    f = Figure()
    f.a = A 
    f.b = B 
    return f 

f = figure_creator(10,10)

f.perimeter()
f.a 
f.perimeter()
f.area()
