class Sequence:
    def __init__(self, MESSAGE):
        self.__message = MESSAGE
        

    def __analyze(self):
        answer = self.__message.count('о') 
        return answer 

    #PUBLIC
    def get_answer(self):
        return self.__analyze() 



s = Sequence(input())
print(s.get_answer())



