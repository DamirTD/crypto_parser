Как начать

Предварительные требования

Что вам нужно установить, чтобы запустить проект:
    Docker
    Docker Compose (обычно включено в установку Docker)

Установка

Склонируйте репозиторий в ветке "django-project" на свой локальный компьютер:
```
git clone -b django-project https://github.com/DamirTD/crypto_parser.git
```
Перейдите в каталог проекта:
```
cd crypto_parser
```
Соберите и запустите проект с помощью Docker Compose:
```
docker-compose up --build
```

После успешного выполнения команды, ваше приложение будет доступно по адресу http://localhost:8000/ в вашем веб-браузере
