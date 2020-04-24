import sqlite3 


conn = sqlite3.connect('data.db')
cur = conn.cursor()

salary = []
salary_query="SELECT salary FROM vacancys"
for sal in cur.execute(salary_query):
    salary.append(sal[0])

avg = sum(salary) / len(salary)

d = 0
for s in salary:
    d += (s - avg) ** 2
d = d / len(salary) 
std = d ** 0.5 

print("Average salary:", avg)
print("Std salary:", std)