# Вариант 2
from bs4 import BeautifulSoup as bs 
import requests 

# URL страницы для парсинга
URL = "https://www.scrapethissite.com/pages/simple/"

# Отправляем запрос на указанный URL
response = requests.get(URL)

# Создаем объект BeautifulSoup
soup = bs(response.text, 'html.parser')

# Находим элементы div с классом country на странице
countries = soup.find_all('div', class_='country')

# Находим все элементы div с классом country-info
capitals = soup.find_all("div", class_="country-info")

data_countries = []
data_capitals = []  

for i in countries:
    # Для каждой страны ищем элемент h3 с классом country-name
    country_name_element = i.find("h3", class_="country-name")
    
    # Извлекаем текст
    country_name = country_name_element.text.strip()
    
    # Добавляем страны в список
    data_countries.append(country_name)

for i in capitals:
    # Для каждого элемента ищем span с классом country-capital
    capital_element = i.find("span", class_="country-capital")
    
    # Извлекаем название столицы
    capital_name = capital_element.text.strip()
    
    # Добавляем столицу в список
    data_capitals.append(capital_name)

for i in range(len(data_countries)):
    print(f"{i + 1}. Country: {data_countries[i]}; Capital: {data_capitals[i]};")
