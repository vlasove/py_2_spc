general_list = []

a_set = set([1,2,3])
b_set = set([4,5,6])

general_list.append(a_set)
general_list.append(b_set)
print(general_list)

super_tuple = (1, general_list)
print(super_tuple)
d = {"one":super_tuple}
print(d)

a = [[1,2,3], [3,4,5], [6,7,8]] 