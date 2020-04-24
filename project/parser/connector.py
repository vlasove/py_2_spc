import requests
from bs4 import BeautifulSoup as BS

url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_period=30&text=python&only_with_salary=true&from=cluster_compensation&showClusters=false"

myheaders = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130",
    'accept' : "*/*"
}

#"a!b".split("!") --> ["a", "b"]
def salary_converter(salary):
    pass 
    #1) если salary 120 000-160 000 руб.
    # возвращает 140000
    #2) если salary от 120 000 руб. / до 180 000 руб.
    # возвращается 120000 / 180000
    #3) если salary от 5 000 EUR 
    # возвращается 400000

session = requests.Session()
req = session.get(url, headers=myheaders)
if req.status_code == 200:
    soup = BS(req.content, "lxml")
    vacancy_cards = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
    for card in vacancy_cards:
        title = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text 
        company = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text 
        salary = card.find("span", attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text 

        print(title, company, salary_converter(salary))
else:
    print("ERROR")