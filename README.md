# 🎓 Student Performance Prediction Cloud App

## 📌 Overview

The Student Performance Prediction Cloud App is an end-to-end machine learning web application that predicts a student’s final performance score based on academic and lifestyle inputs such as study hours, sleep hours, attendance, and previous scores.

The application integrates a trained Scikit-learn Gradient Boosting Regressor model with a Flask web interface to provide real-time predictions. It is designed using modular architecture and is cloud-ready, supporting deployment on platforms such as AWS EC2.

This project demonstrates complete machine learning workflow including data preprocessing, feature engineering, model training, model serialization, web integration, and cloud deployment.

---

## 🚀 Features

* Predict student performance using machine learning model
* Interactive web interface using Flask
* Feature preprocessing and scaling using StandardScaler
* Gradient Boosting Regression model integration
* Modular and scalable project structure
* Logging for monitoring and debugging
* Cloud deployment ready (AWS EC2 compatible)

---

## 🧠 Machine Learning Details

* Algorithm: GradientBoostingRegressor
* Library: Scikit-learn
* Model file: `models/model.pkl`
* Scaler file: `models/scaler.pkl`

### Input Features:

* Study Hours
* Sleep Hours
* Attendance
* Previous Scores
* Extracurricular Activities

### Process Flow:

User Input → Flask App → Data Scaling → ML Model → Prediction → Display Result

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML, CSS
* Joblib
* AWS EC2 (Cloud Deployment)

---

## 📁 Project Structure

```
student_performance_cloud_app/

app.py                 # Flask web application
model.py               # Model training script
utils.py               # Utility functions
generate_data.py       # Dataset generation script

data/
students.csv           # Dataset

models/
model.pkl              # Trained ML model
scaler.pkl             # Feature scaler

templates/
index.html             # Web interface

static/
style.css              # Styling

logs/
app.log
model.log

requirements.txt       # Dependencies
README.md              # Documentation
student-key.pem        # AWS deployment key
```

---

## ⚙️ Installation

Install required dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧪 Train the Model (Optional)

To retrain the model:

```
python model.py
```

---

## ☁️ Cloud Deployment (AWS EC2)

Connect to EC2 instance:

```
ssh -i student-key.pem ec2-user@your-public-ip
```

Install dependencies:

```
pip install -r requirements.txt
```

Run application:

```
python app.py
```

Access application via:

```
http://your-public-ip:5000
```

---

## 📊 Skills Demonstrated

* Machine Learning Model Development
* Data Preprocessing and Feature Engineering
* Model Serialization and Deployment
* Flask Web Application Development
* Cloud Computing (AWS EC2)
* Full Stack Machine Learning Application

---

## 🎯 Project Objective

To build a scalable and cloud-deployable machine learning application capable of predicting student performance and demonstrating real-world ML engineering and deployment skills.

---

## 👩‍💻 Author

Aishwarya Boda
Machine Learning and Cloud Computing Project

---
