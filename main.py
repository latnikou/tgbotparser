from bs4 import BeautifulSoup
import requests

url = 'https://www.vidal.ru/analog/search?product=%D0%B0%D0%B1%D0%B0%D0%BA%D0%B0%D0%B2%D0%B8%D1%80&type=full&ProductID='

response = requests.get(url);
print(response)
bs = BeautifulSoup(response.text, 'lxml')
temp = bs.find('td', 'products-table-name')
print(temp.text)