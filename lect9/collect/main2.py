class Stack:
    def __init__(self):
        self.__values = []

    def add(self, element):
        self.__values.append(element)

    def pop(self):
        return self.__values.pop()

    def empty(self):
        return  len(self.__values) == 0
    
    def clear(self):
        self.__values.clear()

    def __str__(self):
        answer = ""
        for i in self.__values:
            answer += str(i) + " "
        return answer 

s = Stack()
s.add(20)
s.add(30)
s.add(40)
s.pop()
s.clear()
print(s.empty())

