import datetime
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def find_and_extract(soup, element_type, class_name_selector, class_name_selector_alt, default="Not Found"):
    element = soup.find(element_type, class_=class_name_selector)
    if not element:
        element = soup.find(element_type, class_=class_name_selector_alt)

    if element:
        return element.text.strip()
    else:
        return default

# Функция для парсинга биткоина
def get_cryptocurrency_info(request):
    crypto_info = None

    if request.method == 'POST':
        user_input = request.POST.get('crypto_input', '').strip()
        url = f'https://coinmarketcap.com/currencies/{user_input.replace(" ", "-")}/'

        response = requests.get(url)

        if '-' in user_input:
            price_class = 'sc-16891c57-0 ksCNvw base-text'
            price_class_alt = 'sc-16891c57-0 dxubiK base-text'
        else:
            price_class = 'sc-16891c57-0 dxubiK base-text'
            price_class_alt = 'sc-16891c57-0 ksCNvw base-text'

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            topicID_element = find_and_extract(soup, 'span', class_name_selector='sc-16891c57-0 dMKlNV base-text', class_name_selector_alt='some-other-class')
            topicName_element = find_and_extract(soup, 'span', class_name_selector='coin-name-pc', class_name_selector_alt='another-class')
            topicPrice_element = find_and_extract(soup, 'span', class_name_selector=price_class, class_name_selector_alt=price_class_alt)

            if topicID_element and topicName_element and topicPrice_element:
                crypto_info = {
                    'id': topicID_element,
                    'name': topicName_element,
                    'price': topicPrice_element,
                }
            else:
                crypto_info = {'error': 'Данные не найдены'}

    return render(request, 'crypto_parser/index.html', {'crypto_info': crypto_info})
