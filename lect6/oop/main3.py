class Regular:
    def __init__(self, salary = 70000):
        self.salary = salary

    def pay(self):
        return self.salary  

class Freelancer:
    def __init__(self, hours=1, mph=1):
        self.hours = hours
        self.mph = mph 

    def pay(self):
        return self.hours * self.mph 

class Intern:
    def __init__(self, base=25000, bonus=0):
        self.base = base 
        self.bonus = bonus 

    def pay(self):
        return self.base + (self.base*self.bonus) 

state = []
state.append(Regular(1000000))
state.append(Regular(760000))
state.append(Regular())
state.append(Freelancer(45, 7))
state.append(Freelancer(32, 6.9))
state.append(Intern(bonus=1))

total_amount=0
for person in state:
    total_amount += person.pay()
print(total_amount)