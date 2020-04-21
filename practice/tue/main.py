class Sequence:
    def __init__(self, MESSAGE):
        self.message = MESSAGE

    def analyze(self):
        answer = self.message.count('о') 
        return answer 

    def get_answer(self):
        return self.analyze() 



s = Sequence(input())
print(s.get_answer())