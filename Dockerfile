FROM python:3.11-slim
# Установка зависимостей системы, если нужны
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     ...
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Переменная окружения для версии (будет переопределяться в docker-compose)
ENV MODEL_VERSION=v1.0.0

EXPOSE 8080

# Запуск Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]