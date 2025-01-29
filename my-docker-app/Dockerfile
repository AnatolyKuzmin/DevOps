# Используйте официальный образ Python как базовый
FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файл requirements.txt и установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальной код приложения
COPY . .

# Укажите команду для запуска приложения
CMD ["python", "app.py"]

