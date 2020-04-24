from models.vacancy import Vacancy
from parsers.connector import Parser

from tqdm import tqdm

region = int(input())
search_requet = input()
BASE_URL="https://hh.ru/search/vacancy?area={}&clusters=true&enable_snippets=true&search_period=30&text={}&only_with_salary=true&from=cluster_compensation&showClusters=false&page=%i".format(region, search_requet)



p = Parser(BASE_URL%(0))
last_page = p.get_last_page()
for j in tqdm(range(0, last_page + 1)):
    current_parser = Parser(BASE_URL%(j))
    current_parser.get_info()
    for vac in current_parser.vacancy_bag:
        new_vac = Vacancy(vac[0], vac[1], vac[2])
        new_vac.save()
