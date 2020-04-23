from models.vacancy import Vacancy

v = Vacancy("Python Developer", "Yandex", 120000)
v1 = Vacancy("Python Dev + JS", "Avito", 115000)

v.save()
v1.save()

region = int(input())
search_requet = input()

base_url = "https://hh.ru/search/vacancy?area={}&clusters=true&enable_snippets=true&search_period=30&text={}&only_with_salary=true&from=cluster_compensation&showClusters=false".format(region, search_requet)
print(base_url)