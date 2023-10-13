# Импорт библиотек
import requests
from bs4 import BeautifulSoup

# Ссылка сайта с которого берем значение
url = 'https://coinmarketcap.com/en/currencies/bitcoin/'

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ишем значения и присваиваем в переменную
    name = soup.find('span', class_='coin-name-pc').text.strip()
    symbol = soup.find('span', class_='sc-16891c57-0 dMKlNV base-text').text.strip()
    price = soup.find('span', class_='sc-16891c57-0 dxubiK base-text').text.strip()

    print(f'Название: {name}')
    print(f'Монета: {symbol}')
    print(f'Цена: {price}')
else :
    print("Ошибка!")
