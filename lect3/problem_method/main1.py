class Figure:
    a = 0 
    b = 0


# f: arg of Figure class
def perimeter(f):
    return 2*(f.a + f.b)

# f: arg of Figure class 
def area(f):
    return f.a * f.b 



def figure_creator(A,B):
    f = Figure()
    f.a = A 
    f.b = B 
    return f 



f = figure_creator(10, 10)
f1 = figure_creator(5, 10)

print("Perimeter of figure:", perimeter(f))
print("Area of figure:", area(f))

print("Perimeter of figure:", perimeter(f1))
print("Area of figure:", area(f1))