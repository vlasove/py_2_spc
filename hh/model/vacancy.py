import sqlite3

class Vacancy:
    def __init__(self, title, short_story, company, salary):
        self.__title = title 
        self.__short_story = short_story 
        self.__company = company 
        self.__salary = salary 


    def get_vacancy(self):
        return (self.__title, self.__short_story, self.__company, self.__salary)

    def save(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = ..... 

        cur.execute(query,....)

        conn.commit()
        conn.close()


v = Vacancy("MOSOBLBANCK", "COFFEE, PYTHON, SALTO", "SUPER BIG", "100 000")
v.save()

    