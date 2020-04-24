class Film:
    title = ""
    duration = -1 

    def creator(self, TITLE, DURATION):
        self.title = TITLE
        self.duration = DURATION


    def time_left(self, time_now):
        left = self.duration - time_now
        return left 

#f = Film() + f.creator("LOTR" ,240)
f = Film()
f.creator("HP",123)

print(f.title, f.duration)



f.time_left(115) # 125