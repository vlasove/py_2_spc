numbers = [1,2,3,4,5,6,7,8,9,10,1,2,3,1,3,1,31,2]

for i in range(18):
    print("Numbers size (b):", numbers.__sizeof__(), "Len:",len(numbers))
    numbers.pop()


Garbage Collector == сборщик мусора