database = []

 
class Vacancy:
    def __init__(self, title, salary):
        self.__id = len(database) + 1
        self.__title = title 
        self.__salary = salary 

        self.__add_vacancy()

    def __add_vacancy(self):
        database.append(self)

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return "{} {} {}".format(self.__id , self.__title, self.__salary)
 
def average_salary(db):
    total_salary = 0
    for v in db:
        total_salary += v.get_salary()
    return total_salary / len(db)

def std_salary(db):
    pass 


print(database, len(database))
v1 = Vacancy("python", 10)
v2 = Vacancy("javascript", 11)
v3 = Vacancy("php", 9)
v4 = Vacancy("golang", 22)
v4 = Vacancy("c++", 14)

print("Average salary:", average_salary(database))