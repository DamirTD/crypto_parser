import datetime
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Функция для парсинга биткоина
def get_cryptocurrency_info(request):
    crypto_info = None

    if request.method == 'POST':
        user_input = request.POST.get('crypto_input', '').strip()
        url = f'https://coinmarketcap.com/currencies/{user_input}/'

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            topicID_element = soup.find('span', class_='sc-16891c57-0 dMKlNV base-text')
            topicName_element = soup.find('span', class_='coin-name-pc')
            topicPrice_element = soup.find('span', class_='sc-16891c57-0 dxubiK base-text')

            if topicID_element and topicName_element and topicPrice_element:
                crypto_info = {
                    'id': topicID_element.text.strip(),
                    'name': topicName_element.text.strip(),
                    'price': topicPrice_element.text.strip(),
                }
            else:
                crypto_info = {'error': 'Данные не найдены'}

    return render(request, 'crypto_parser/index.html', {'crypto_info': crypto_info})