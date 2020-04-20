d = {"one":[1,2,3,4,5], "two": 2, "three":3, (1,2,3) : 20}
print(d)
print(d["one"])
print(d[(1,2,3)])

print(len(d))
d["four"] = 4
print(d)

for key in d.items(): #d.keys() + d.values()
    print(key)
