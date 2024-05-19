# FastAPI Clean Template

FastAPI Clean Template - это шаблон проекта на FastAPI, включающий базовую настройку базы данных PostgreSQL и механизм авторизации пользователей с использованием JWT токенов. Этот шаблон предназначен для ускорения начала разработки новых проектов, предоставляя готовую структуру и базовые функции.

## Содержание

- [Установка](#установка)
- [Запуск](#запуск)
- [Документация](#документация)
- [Авторизация](#авторизация)
- [Структура проекта](#структура-проекта)

## Установка

1. Склонируйте или скачайте репозиторий:
   ```bash
   git clone https://github.com/your-username/FastAPI-clean-template.git
   cd FastAPI-clean-template

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Windows используйте .venv\Scripts\activate

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

## Запуск
После выполнения вышеуказанных шагов, проект будет доступен по адресу http://localhost/

## Документация
Документация доступна по адресу http://localhost/docs#/

## Авторизация
Проект включает систему авторизации пользователей с использованием JWT токенов. Вот краткое описание основных функций:

1. Регистрация пользователя:
- Endpoint: /auth/register/
- Метод: POST
- Тело запроса: { "email": "user@example.com", "password": "password" }
- Описание: Создание нового пользователя с указанным email и паролем.

2. Вход пользователя:
- Endpoint: /auth/login/
- Метод: POST
- Тело запроса: { "email": "user@example.com", "password": "password" }
- Описание: Аутентификация пользователя и создание JWT токена.

3. Выход пользователя:
- Endpoint: /auth/logout/
- Метод: POST
- Описание: Удаление JWT токена.

4. Получение текущего пользователя:
- Endpoint: /auth/me/
- Метод: GET
- Описание: Получение информации о текущем пользователе на основе JWT токена.

## Структура проекта
- alembic/: Директория для управления миграциями базы данных.
  - versions/: Хранение файлов миграций.
  - env.py: Конфигурация Alembic.

- app/: Основная директория проекта.
  - service/: Модуль для бизнес-логики.
  - base.py: Базовые классы и функции.
  - users/: Модуль для управления пользователями и авторизацией.
  - auth.py: Функции для хэширования паролей и создания JWT токенов.
  - dependencies.py: Зависимости для авторизации.
  - models.py: Модели данных пользователей.
  - router.py: Роутеры для авторизации и управления пользователями.
  - schemas.py: Pydantic схемы для пользователей.
  - service.py: Сервисы для управления пользователями.
  - config.py: Конфигурация приложения.
  - database.py: Настройки подключения к базе данных.
  - exception.py: Пользовательские исключения.
  - main.py: Главный файл для запуска приложения.