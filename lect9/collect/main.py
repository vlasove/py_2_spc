import collections

c_counter = collections.Counter()
print(c_counter, type(c_counter))

words = ['a', 'b', 'c', 'd', 'a', 'b','a','c','a','e']
counter_dict = {}

for word in words:
    if word in counter_dict.keys():
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1 

print(counter_dict)

for word in words:
    c_counter[word] += 1

print(c_counter)
print(c_counter["a"], c_counter["c"])

print(list(c_counter.elements()))
print(c_counter.most_common(3))