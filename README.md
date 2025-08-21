# Stripe Django Ecommerce Store

Этот проект — пример интернет-магазина на Django с интеграцией Stripe для обработки платежей.

## Описание

- **Backend:** Django
- **Платежная система:** Stripe
- **База данных:** SQLite (по умолчанию)
- **Docker:** Поддерживается запуск через Docker Compose

### Основные возможности
- Просмотр товаров
- Детальная страница товара
- Оформление заказа с оплатой через Stripe
- Админка Django


## Действующий пример
- Сайт
```url
https://ecomm.dmace.keenetic.pro/
```
 - Админка (login: admin, pass: admin)
```url
https://ecomm.dmace.keenetic.pro/admin
```

### Описание
Проект запущен на моем raspberry pi 5 сервере, так как у меня серый Ip, подключится к нему удаленно не получится, а домен предоставляет мой роутер

## Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/DmitryAce/stripe-django
cd stripe-django
```

### 2. Настройка переменных окружения

Скопируйте файл `example.env` в `.env` и укажите свои значения:
```bash
copy example.env .env  # Windows
# или
cp example.env .env    # Linux/Mac
```

### 3. Запуск через Docker (рекомендуется)

```bash
docker-compose up --build
```

- Приложение будет доступно по адресу: http://localhost:8089
- Админка: http://localhost:8089/admin/

### 4. Локальный запуск без Docker

#### Установка зависимостей
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

#### Миграции и запуск сервера
```bash
python manage.py migrate
python manage.py runserver
```

### 5. Создание суперпользователя (для доступа к админке)
```bash
python manage.py createsuperuser
```

## Структура проекта
- `ecommerce_store/` — настройки и корневой модуль Django
- `items/` — приложение с товарами
- `templates/` — HTML-шаблоны
- `static/`, `staticfiles/` — статика
- `nginx/` — конфигурация nginx для продакшена

## Переменные окружения
- `STRIPE_SECRET_KEY` — секретный ключ Stripe
- `STRIPE_PUBLISHABLE_KEY` — публичный ключ Stripe
- `DJANGO_SECRET_KEY` — секретный ключ Django
- `DEBUG` — режим отладки (True/False)
---
