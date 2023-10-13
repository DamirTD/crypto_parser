# Импорт библиотек
import requests
from bs4 import BeautifulSoup

while True:
    # Ввод пользователя
    user_input = input("Enter a cryptocurrency ID or Name (or 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        break  # Выйти если пользователь напишет 'exit'

    # URL сопоставляем с вводом пользователя
    url = f'https://coinmarketcap.com/currencies/{user_input}/'

    # Отправка GET запроса
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Названия
        topicID_element = soup.find('span', class_='sc-16891c57-0 dMKlNV base-text')# ID
        if topicID_element:
            topicID = topicID_element.text.strip()
        else :
            topicID = "error"
        topicName_element = soup.find('span', class_='coin-name-pc') # Name
        if topicName_element:
            topicName = topicName_element.text.strip()
        else :
            topicName = "error"
        topicPrice_element = soup.find('span', class_='sc-16891c57-0 dxubiK base-text') # Price
        if topicPrice_element:
            topicPrice = topicPrice_element.text.strip()
        else :
            topicPrice = "error"
        # topicMarketCap_element = soup.find('p', class_='sc-16891c57-0 fRWxhs base-text') # Market Cap
        # if topicMarketCap:
        #     topicMarketCap = topicMarketCap_element.text.strip()
        # else :
        #     topicMarketCap = "error"
        # topicVolume_element = soup.find('p', class_='sc-16891c57-0 fRWxhs base-text') # Volume 
        # if topicVolume_element:
        #     topicVolume = topicVolume_element.text.strip()
        # else :
        #     topicVolume = "error"
        # topicCirculatingSupply_element = soup.find('p', class_='text slider-value') # Circulating Supply
        # if topicCirculatingSupply_element:
        #     topicCirculatingSupply = topicCirculatingSupply_element.text.strip()
        # else :
        #     topicCirculatingSupply = "error"

            #todo: Graphics
        
        print(f'Name: {topicID}')
        print(f'Name: {topicName}')
        print(f'Price: {topicPrice}')
        # print(f'MarketCap: {topicMarketCap}')
        # print(f'Volume: {topicVolume}')
        # print(f'Circulating Supply: {topicCirculatingSupply}')

        

    else :
        print("Ошибка!")
