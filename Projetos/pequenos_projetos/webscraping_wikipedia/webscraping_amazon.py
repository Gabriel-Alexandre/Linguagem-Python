import requests
from bs4 import BeautifulSoup

#especifique o URL
url = "https://www.amazon.com.br/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

result = soup.find_all('div', attrs={"class": "a-cardui-header"})

for v in result:
    try:
        titulo = v.find('h2', attrs={"class": "a-color-base headline truncate-2line"})
        print(titulo.text)
    except:
        print("error")