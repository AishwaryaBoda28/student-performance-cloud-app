from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import logging
from utils import validate_input

app = Flask(__name__)

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

@app.route("/", methods=["GET","POST"])
def index():
    prediction = None

    if request.method == "POST":
        data = [
            request.form["study"],
            request.form["sleep"],
            request.form["attendance"],
            request.form["previous"],
            request.form["extra"]
        ]

        vals = validate_input(data)

        if vals:
            df = pd.DataFrame([vals], columns=[
                "study_hours","sleep_hours",
                "attendance","previous_score",
                "extra_classes"
            ])

            df["study_sleep_ratio"] = df["study_hours"]/df["sleep_hours"]
            df["effort_score"] = df["study_hours"]*df["attendance"]

            X = scaler.transform(df)

            pred = model.predict(X)[0]
            prediction = round(pred,2)

            logging.info(f"Prediction: {prediction}")
        else:
            prediction = "Invalid Input"

    return render_template("index.html", prediction=prediction)


@app.route("/api/predict", methods=["POST"])
def api():
    data = request.json["values"]
    vals = validate_input(data)

    if vals:
        df = pd.DataFrame([vals])
        pred = model.predict(df)[0]
        return jsonify({"prediction":pred})

    return jsonify({"error":"Invalid input"})


if __name__ == "__main__":
    app.run(debug=True)