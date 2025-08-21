FROM python:3.12.2-slim
LABEL authors="dmace"

# Установка зависимостей
RUN apt-get update && apt-get install -y curl && apt-get install -y sqlite3 && apt-get clean
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
RUN pip install psycopg2-binary

# Копирование приложения
COPY . /app
WORKDIR /app

# Настройка переменных среды
ENV DJANGO_SETTINGS_MODULE=ecommerce_store.settings

# Подготовка скрипта для запуска
COPY boot.sh /app/boot.sh
RUN chmod +x /app/boot.sh

# Открытие порта приложения
EXPOSE 5000

# Команда для запуска
ENTRYPOINT ["./boot.sh"]
