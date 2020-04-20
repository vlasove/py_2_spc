# set() Множество -коллекция, хранящая уникальный объекты, не индексируемая => не упорядоченная
a_set = set([1,1,2,3,4,2,1,1,3,45,1,0])

print(a_set)

print("Length set:", len(a_set))
print("Sum elems of set:", sum(a_set))

print("Max/min in set:", max(a_set), min(a_set))

if 3 in a_set:
    print("YES, 3 IN SET")

