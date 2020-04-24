import requests
from bs4 import BeautifulSoup as BS


class Parser:
    headers = {
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130",
        'accept' : "*/*"
    }

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.vacancy_bag = []

    def check_connection(self):
        if self.session.get(self.base_url, headers=self.headers).status_code == 200:
            return True 
        else:
            return False 

    def get_last_page(self):
        if self.check_connection():
            soup = BS(self.session.get(self.base_url, headers=self.headers).content, "lxml")
            pages = soup.find_all("a", attrs={"data-qa":"pager-page"})
            return int(pages[-1].text)

    def parse_salary(self, salary):
        currency = {"руб.":1, "EUR" : 80, "USD":75}
        words_list = salary.split()
        try:
            answer = int(words_list[1]) * 1000
        except:
            answer = int((int(words_list[0]) + int(words_list[1].split('-')[1]))/2) * 1000
        return answer * currency[words_list[-1]]

    def get_info(self):
        if self.check_connection():
            soup = BS(self.session.get(self.base_url, headers=self.headers).content, "lxml")
            vacancy_cards = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
            for card in vacancy_cards:
                try:
                    title = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text 
                    company = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text 
                    salary = card.find("span", attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text 

                    self.vacancy_bag.append([title, company, self.parse_salary(salary)])
                except:
                    pass 







# url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_period=30&text=python&only_with_salary=true&from=cluster_compensation&showClusters=false&page=0"

# myheaders = {
#     'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130",
#     'accept' : "*/*"
# }

# def get_last_page():
#     session = requests.Session()
#     req = session.get(url, headers=myheaders)
#     if req.status_code == 200:
#         soup = BS(req.content, "lxml")
#         pages = soup.find_all("a", attrs={"data-qa":"pager-page"})
#         return int(pages[-1].text)

# get_last_page()


# def salary_converter(salary):
#     currency = {"руб.":1, "EUR" : 80, "USD":75}
#     words_list = salary.split()
#     try:
#         answer = int(words_list[1]) * 1000
#     except:
#         answer = int((int(words_list[0]) + int(words_list[1].split('-')[1]))/2) * 1000
#     return answer * currency[words_list[-1]]

# session = requests.Session()
# req = session.get(url, headers=myheaders)
# if req.status_code == 200:
#     soup = BS(req.content, "lxml")
#     vacancy_cards = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
#     for card in vacancy_cards:
#         title = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text 
#         company = card.find("a", attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text 
#         salary = card.find("span", attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text 

#         print(title, company, salary_converter(salary))
        
# else:
#     print("ERROR")