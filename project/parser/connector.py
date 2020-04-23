import requests

url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_period=30&text=химик&only_with_salary=true&from=cluster_compensation&showClusters=false"

myheaders = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130",
    'accept' : "*/*"
}

session = requests.Session()
req = session.get(url, headers=myheaders)
if req.status_code == 200:
    print(req.content)
else:
    print("ERROR")