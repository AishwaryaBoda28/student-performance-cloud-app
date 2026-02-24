import pandas as pd
import numpy as np
import joblib
import logging
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

os.makedirs("models", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename="logs/model.log", level=logging.INFO)

def train():

    data = pd.read_csv("data/students.csv")

    # Feature Engineering
    data["study_sleep_ratio"] = data["study_hours"] / data["sleep_hours"]
    data["effort_score"] = data["study_hours"] * data["attendance"]

    X = data.drop("final_score", axis=1)
    y = data["final_score"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    logging.info(f"MAE: {mae}, R2: {r2}")

    joblib.dump(model, "models/model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    print("Model saved")
    print("MAE:", mae)
    print("R2:", r2)

if __name__ == "__main__":
    train()