a_list = [123,123,-22,5,12,354123]
a_list.append(-10000)
print(a_list)

a_list[0] = 22
print(a_list)

a_list.sort(reverse=True)
print(a_list)

del a_list[0] # удалить по индексу
a_list.pop() # удалить последний