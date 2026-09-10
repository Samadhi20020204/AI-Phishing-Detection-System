from fastapi import FastAPI
from pydantic import BaseModel

from ml_model.predict import predict_url


# Create FastAPI application
app = FastAPI(
    title="AI-Based Phishing Detection API",
    description="API for detecting phishing URLs using Machine Learning",
    version="1.0.0"
)


# Request data format
class URLRequest(BaseModel):
    url: str


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI-Based Phishing Detection API is running"
    }


# URL prediction endpoint
@app.post("/predict")
def predict(request: URLRequest):

    result = predict_url(request.url)

    return {
        "url": request.url,
        "prediction": result
    }