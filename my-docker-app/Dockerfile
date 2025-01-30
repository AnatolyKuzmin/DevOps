# Используем официальный образ Python как базовый
FROM python:3.9-slim

# Установим рабочую директорию
WORKDIR /app

# Скопируем файл requirements.txt и установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем остальной код приложения
COPY . .

# Укажем команду для запуска приложения
CMD ["python", "app.py"]

