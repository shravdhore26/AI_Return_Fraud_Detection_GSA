from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# path to model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "fraud_model.pkl")

model = joblib.load(MODEL_PATH)


class Input(BaseModel):

    num_returns: int
    refund_amount: float
    time_gap: int
    mismatch: int
    category_risk: int
    loyalty: int
    reason_pattern: int


@app.post("/predict")

def predict(data: Input):

    features = np.array([[
        data.num_returns,
        data.refund_amount,
        data.time_gap,
        data.mismatch,
        data.category_risk,
        data.loyalty,
        data.reason_pattern
    ]])

    # ML probability
    prob = model.predict_proba(features)[0][1] * 0.75
    fraud_score = round(prob * 100, 2)

    return {"fraud_probability_percent": fraud_score}


@app.post("/explain")

def explain(data: Input):

    reasons = []

    if data.num_returns > 4:
        reasons.append("High return frequency")

    if data.refund_amount > 3000:
        reasons.append("Large refund value")

    if data.time_gap < 3:
        reasons.append("Very quick return after purchase")

    if data.mismatch == 1:
        reasons.append("Product mismatch detected")

    if data.category_risk >= 4:
        reasons.append("High-risk product category")

    if data.loyalty < 3:
        reasons.append("Low customer loyalty")

    if not reasons:
        reasons.append("Customer behaviour appears normal")

    return {"explanation": "Top Risk Factors → " + ", ".join(reasons)}