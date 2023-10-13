# Импорт библиотек
from email.message import EmailMessage
import ssl
import smtplib
import requests
from bs4 import BeautifulSoup

# Функция для поиска и извлечения информации из HTML-страницы 
def find_and_extract(soup, element_type, class_name, default="Not Found"):
    element = soup.find(element_type, class_=class_name)        # Ищем элемент на странице с заданным типом и классом
    if element:                                                 # Если нашли элемент. element = topicID, topicName, topicPrice
        return element.text.strip()
    else:                                                       # В случае если не нашли элемент
        return default

while True:
    # Криптовалюта которую нужно отправить
    user_input = "bitcoin"

    user_input = user_input.replace(" ", "-")                   # Меняем пробел на тире, для того чтобы в url значение input-a было через тире.
    if '-' in user_input:                                       # Из-за того что классы с пробелом и без разные, то выводить нужно соответственно разные классы
        price_class = 'sc-16891c57-0 ksCNvw base-text'
    else:                                                       # В случае если введенное пользователем значение не имеет пробелов и тире.
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

        # Код для отправки электронной почты из sendEmail.py
        email_sender = 'toriya.damir.2004@gmail.com'
        email_password = 'naxw iweb jpke xzyu'
        email_reciver = 'toriadamir34@gmail.com'

        subject = f'Информация о криптовалюте {user_input}'
        body = f"""
        Name: {topicID}
        Name: {topicName}
        Price: {topicPrice}
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())
    
    else :
        print("Ошибка!")
