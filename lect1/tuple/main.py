a_tuple = (1,12,3,12,312,3,213)
# tuple() кортеж - "неизменяемый список"
a_tuple[0:5]

for item in a_tuple:
    print(item)


a_list = [1,2,3,4,5,6,7]
a_tuple = (1,2,3,4,5,6,7)

print(a_list.__sizeof__())
print(a_tuple.__sizeof__())