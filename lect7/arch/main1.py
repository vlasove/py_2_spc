import pickle 

class A:
    a = 1 

o = A()

with open("a_class.pickle", "wb") as f:
    pickle.dump(o, f)

p = pickle.dumps(o)
print(p)

with open("a_class.pickle", "rb") as f:
    s = pickle.load(f)

# pickle.loads()
# print(s)
