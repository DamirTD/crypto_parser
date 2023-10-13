# Используем образ Python в качестве базового образа
FROM python:3.8

# Устанавливаем переменную окружения для предотвращения вывода
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочий каталог
WORKDIR /crypto_parser/crypto_project  

# Копируем зависимости проекта в контейнер
COPY requirements.txt /crypto_parser/crypto_project/ 

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /crypto_parser/crypto_project/  


# Запускаем команду для запуска Django приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]