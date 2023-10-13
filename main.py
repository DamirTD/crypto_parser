# Импорт библиотек
import requests
from bs4 import BeautifulSoup

def find_and_extract(soup, element_type, class_name, default="Not Found"):
            element = soup.find(element_type, class_=class_name)
            if element:
                return element.text.strip()
            else:
                return default

while True:
    # Ввод пользователя
    user_input = input("Enter a cryptocurrency ID or Name (or 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        break  # Выйти если пользователь напишет 'exit'

    user_input = user_input.replace(" ", "-")

    if '-' in user_input:
        price_class = 'sc-16891c57-0 ksCNvw base-text'
    else:
        price_class = 'sc-16891c57-0 dxubiK base-text'

    # URL сопоставляем с вводом пользователя
    url = f'https://coinmarketcap.com/currencies/{user_input}/'  

    # Отправка GET запроса
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        topicID = find_and_extract(soup, 'span', 'sc-16891c57-0 dMKlNV base-text')
        topicName = find_and_extract(soup, 'span', 'coin-name-pc')
        topicPrice = find_and_extract(soup, 'span', price_class)
        
        print(f'Name: {topicID}')
        print(f'Name: {topicName}')
        print(f'Price: {topicPrice}')

    else :
        print("Ошибка!")
