# Образовательный портал. 
Веб-приложение образовательный портал.
## Краткое описание
Образовательный портал имеет базовую функциональность, предоставляет регистрацию и авторизацию пользователей, предоставляет удобную интегрированную админ-панель.
# Установка и запуск веб-приложения
### 1. Клонирование репозитория 
`git clone https://github.com/technonavigator/educationapp/`
### 2. Переход в директорию проекта
`cd app`
### 3. Создание виртуального окружения 
`python -m venv .venv`
### 4. Активация виртуального окружения
Для windows:
`.venv\scripts\activate`
Для linux:
`.venv/bin/activate`
### 5. Установка необходимых зависимостей 
`pip install -r requirements.txt`
### 6. Запуск сервера
`python manage.py runserver`
После выполнения установки по адресу http://127.0.0.1:8000/ будет доступен тестовый сервер.
# Создание суперпользователя (администратора)
`python manage.py createsuperuser`
# Стек использованных пакетов
1. Django rest framework
2. Pillow
3. Bootstrap
4. SQLite
5. SQLAlchemy
# Демонстрация работы проекта
https://rutube.ru/video/private/ef14ef443ff300f7b31dc7f98a7996b2/?p=PherresjEOKjdZT5SBOuhw
