class SmartList:
    def __init__(self, words = []):
        self.__words = words 

    def add(self, word):
        self.__words.append(word)
        self.__sorted__()

    def __sorted__(self):
        self.__words.sort(key=custom_sort) 

    def get_answer(self):
        for word in self.__words:
            print(word)


def custom_sort(word):
    return (len(word) , word)

sl = SmartList()
n = int(input())
for i in range(n):
    word = input()
    sl.add(word)

sl.get_answer()



    