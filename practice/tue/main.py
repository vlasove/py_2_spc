class Sequence:
    def __init__(self, MESSAGE):
        self.__message = MESSAGE

    def __analyze(self):
        return len(max(self.__message.split('р')))  

    def get_answer(self):
        return self.__analyze() 



s = Sequence(input())
print(s.get_answer())