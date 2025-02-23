# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем и устанавливаем зависимости
COPY requirements.txt .
COPY pytest.ini .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install pytest  # Добавляем установку pytest

# Создаем директорию для данных
RUN mkdir /app/data

# Копируем код приложения
COPY . .
COPY app/ app/
COPY tests/ tests/

# Проверяем права на директорию с данными
RUN chmod -R 755 /app/data

# Открываем порт
EXPOSE 8000

# Используем скрипт запуска
CMD ["python", "main.py"]