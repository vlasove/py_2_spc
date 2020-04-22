import pickle 

data = [
    {
        "id":1,
        "login":"Bob9000",
        "email":"bob@bob.ru"
    },
    {
        "id":2,
        "login":"Jack",
        "email":"lack@yandex.ru"
    },
    None
]

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)

print(data_new, type(data_new), len(data_new))