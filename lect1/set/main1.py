a_set = set([1,2,3,4])
b_set = set([3,4,5,6])

c_set = a_set.union(b_set)
print("Union:", c_set)

d_set = a_set.intersection(b_set)
print("Intersection:", d_set)

e_set = a_set - b_set 
print("Diff:", e_set)