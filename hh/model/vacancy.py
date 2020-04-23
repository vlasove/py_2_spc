import sqlite3 
import create_table


class Vacancy:
    def __init__(self, title, salary):
        self.__id = None
        self.__title = title 
        self.__salary = salary 

        self.__add_vacancy()

    def __add_vacancy(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = "INSERT INTO vacancys VALUES(NULL, ?,?)"
        cur.execute(query_insert, (self.__title, self.__salary))

        conn.commit()
        conn.close()


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
    avg = average_salary(db)
    D = 0
    for v in db:
        D += (v.get_salary() - avg) ** 2
    std = (D / len(db)) ** 0.5
    return std  

    

v1 = Vacancy("python", 10)
v2 = Vacancy("javascript", 11)
v3 = Vacancy("php", 9)
v4 = Vacancy("golang", 22)
v4 = Vacancy("c++", 14)