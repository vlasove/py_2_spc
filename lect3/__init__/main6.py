class Film:
    def __init__(self, TITLE = "" , DURATION = 0):
        self.title = TITLE
        self.duration = DURATION
        

    def time_left(self, time_now):
        left = self.duration - time_now
        return left 

#f = Film() + f.creator("LOTR" ,240)

f = Film("LOTR", 240)

print("Film title:", f.title)
print("Film duration:", f.duration)

f2 = Film()
