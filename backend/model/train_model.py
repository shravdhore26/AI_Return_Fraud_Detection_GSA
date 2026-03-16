import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("fraud_dataset.csv")

# Features and target
X = df.drop("fraud", axis=1)
y = df["fraud"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate accuracy
accuracy = model.score(X_test, y_test)

print("Model accuracy:", round(accuracy,3))

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model saved as fraud_model.pkl")