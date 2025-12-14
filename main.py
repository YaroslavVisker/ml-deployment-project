import os
import pickle
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Заглушка для модели
try:
    with open("model/model.pkl", "rb") as f:
        MODEL = pickle.load(f)
except FileNotFoundError:
    # Создаем фиктивную модель для примера, если файл отсутствует
    class MockModel:
        def predict(self, data):
            # Фиктивная логика предсказания
            return [sum(x) for x in data]
    MODEL = MockModel()

# Версия модели из переменной окружения
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0.0 (default)")

app = FastAPI()

# Схема для входных данных предсказания
class PredictionInput(BaseModel):
    x: list[list[float]]

@app.get("/health")
def health():
    """Возвращает статус и версию модели."""
    return {"status": "ok", "version": MODEL_VERSION}

@app.post("/predict")
def predict(data: PredictionInput):
    """Выполняет инференс."""
    try:
        # В реальной жизни здесь будет: MODEL.predict(data.x)
        predictions = MODEL.predict(data.x)
        return {"predictions": predictions, "version": MODEL_VERSION}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))