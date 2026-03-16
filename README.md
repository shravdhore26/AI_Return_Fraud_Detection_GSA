# AI-Based Return Fraud Detection System

## How to Run the Project

### 1 Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 2 Start Backend Server

Open a terminal and run:

```bash
cd backend
uvicorn main:app --reload
```

Keep this terminal running.

---

### 3 Start Frontend Server

Open a **new terminal** and run:

```bash
cd frontend
start http://127.0.0.1:5500
python -m http.server 5500
```

This will start the frontend server and open the dashboard automatically.


## API Documentation (If you want to access it)

FastAPI automatically provides API documentation at:

```
http://127.0.0.1:8000/docs
```

---

# Overview

This project detects fraudulent return requests in e-commerce platforms using machine learning.

The system analyzes return patterns such as refund amount, return frequency, product mismatch, category risk, and customer loyalty score to estimate the probability of fraud.

A FastAPI backend processes the input data and a dashboard visualizes the fraud risk in real time.

---

# Features

- Machine Learning-based fraud prediction
- Real-time API using FastAPI
- Interactive fraud risk dashboard
- Animated fraud risk gauge
- Fraud alert indicator
- Input validation and reset functionality
- Random test case generator for demo
- Explanation of risk factors

---

# Technologies Used

## Backend
- Python
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- Joblib

## Frontend
- HTML
- CSS
- JavaScript
- Canvas API

## Machine Learning
- Random Forest Classifier

---

# System Architecture

```
User Input → FastAPI Backend → ML Model → Fraud Probability → Dashboard Visualization
```

---

# Folder Structure

```
Return_Fraud_Detection/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── model/
│       ├── generate_data.py
│       ├── train_model.py
│       ├── fraud_dataset.csv
│       └── fraud_model.pkl
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── firebase/
│   └── firebase_config.js
│
└── README.md
```

---

# Dataset Generation

Synthetic transaction data is generated to simulate real-world return behaviors including:

- number of returns
- refund amount
- time gap between purchase and return
- product mismatch indicator
- product category risk
- customer loyalty score
- return reason pattern

Dataset size: **20,000 records**

---

# Model Training

A **Random Forest classifier** is trained to predict fraud probability.

Example features used:

- return frequency
- refund value
- return timing
- mismatch detection
- category risk
- loyalty score

---

# Example Prediction

Example Input:

```
Returns: 6
Refund: 4200
Time gap: 2
Mismatch: 1
Category risk: 4
Loyalty: 3
```

Output:

```
Fraud Score: 82%
Prediction: FRAUD
⚠ FRAUD ALERT
```

---

# Future Improvements

- Integration with real transaction datasets
- Model explainability using SHAP
- User authentication
- Fraud monitoring dashboard for multiple transactions
- Cloud deployment

---

# Team

**Team Name:** NexaTech

Members:

- Shravani Mahesh Dhore (Team Leader)
- Purva Pendbhaje
- Rutuja Yadav

Program:  
M.Sc Data Science & Big Data Analytics  
MIT-WPU, Pune