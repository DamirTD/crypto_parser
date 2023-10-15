Проект распределен по веткам. Ветка main не главная

Команды Git которые использовались в командной работе

    git clone 'ссылка' - Клонирует репозиторий
    
    git clone -b 'ветка' 'ссылка' - Клонирует определенную ветку с репозитория
    git remote add origin "ссылка на репозиторий" - устанавливает соединение 

    git branch - Просмотреть ветки
    git branch -D 'название' - Удаляет ветку
    git checkout 'название ветки' - Подключиться к ветке
    
    git checkout -b 'название' - Создает отдельную ветку
    git add . - Добавляет все файлы
    git commit -m "сообщение" - Отправляет коммит
    git push origin 'название' - Пушит проект
    git push origin --delete 'название ветки' - Удаляет ветку

    git commit --amend -m "исправленный текст в коммите" - Исправляет последний коммит   

    git pull origin main - Извлекает основную ветку
