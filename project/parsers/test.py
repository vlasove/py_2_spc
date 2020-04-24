#"a!b".split("!") --> ["a", "b"]
def salary_converter(salary):
    currency = {"руб.":1, "EUR" : 80, "USD":75}
    words_list = salary.split()
    print(words_list) 
    try:
        answer = int(words_list[1]) * 1000
    except:
        answer = int((int(words_list[0]) + int(words_list[1].split('-')[1]))/2) * 1000
    return answer * currency[words_list[-1]]
    #1) если salary 120 000-160 000 руб.
    # возвращает 140000
    #2) если salary от 120 000 руб. / до 180 000 руб.
    # возвращается 120000 / 180000
    #3) если salary от 5 000 EUR 
    # возвращается 400000

a = "120 000-220 000 руб."
b = "от 250 000 руб."
c = "от 2 000 EUR"

print(salary_converter(a))
print(salary_converter(b))
print(salary_converter(c))