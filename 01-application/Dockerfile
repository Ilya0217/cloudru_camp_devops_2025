# Инициалищируем образ
FROM python:3.12-slim

# Устанавливаем зависимости
RUN pip install fastapi uvicorn

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем приложение в контейнер
COPY app.py .

# Устанавливаем переменную окружения
ENV AUTHOR="Author"

# Запускаем сервер на порту 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
