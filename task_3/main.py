# Вариант 2
from bs4 import BeautifulSoup as bs
import requests 
import json

# URL страницы для парсинга
URL = "https://www.scrapethissite.com/pages/simple/"
# Отправляем запрос
response = requests.get(URL)

soup = bs(response.text, 'html.parser')
countries = soup.find_all('div', class_='country')
capitals = soup.find_all("div", class_ = "country-info")

data_countries = []
data_capitals = []

# Извлекаем текст и очищаем его от лишних пробелов
for i in countries:
    data_countries.append(i.find("h3", class_= "country-name").text.strip())

for i in capitals:
    data_capitals.append(i.find("span", class_ = "country-capital").text.strip())

# Объединяем два списка в словарь
data_dict = dict(zip(data_countries, data_capitals))

for i in range(len(data_countries)):
    print(f"{i + 1}. Country: {list(data_dict.keys())[i]}; Capital: {list(data_dict.values())[i]};")

# Сохраняем полученный словарь в файл JSON
with open("data.json", "w", encoding = "utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)
    print("Данные записаны")
