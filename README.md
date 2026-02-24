# 🎓 Student Performance Prediction Cloud App

## Overview
The Student Performance Prediction Cloud App is an end-to-end machine learning web application that predicts a student’s final performance score based on academic and lifestyle inputs such as study hours, sleep hours, attendance, and previous scores. The application integrates a trained Gradient Boosting Regressor model built using Scikit-learn with a Flask web interface to provide real-time predictions. This project demonstrates complete machine learning workflow including data preprocessing, feature engineering, model training, model serialization, web application integration, and cloud deployment readiness using AWS EC2.

## Features
- Predict student performance using a trained machine learning model
- Interactive and user-friendly web interface built with Flask
- Feature preprocessing and scaling using StandardScaler
- Gradient Boosting Regression model integration for accurate predictions
- Modular and scalable project structure
- Logging system for monitoring and debugging
- Cloud deployment ready and compatible with AWS EC2

## Technologies Used
Python, Flask, Scikit-learn, Pandas, NumPy, HTML, CSS, Joblib, AWS EC2

## Project Structure
student_performance_cloud_app/
app.py – Flask web application
model.py – Model training script
utils.py – Utility and validation functions
generate_data.py – Dataset generation script
data/students.csv – Dataset file
models/model.pkl – Trained machine learning model
models/scaler.pkl – Feature scaler
templates/index.html – Web interface
static/style.css – Styling file
logs/app.log and logs/model.log – Log files
requirements.txt – Project dependencies
README.md – Project documentation

## Installation
Install all required dependencies using the command: pip install -r requirements.txt

## Run the Application
Run the Flask application using the command: python app.py and open the browser at http://127.0.0.1:5000 to access the application.

## Model Training
To retrain the machine learning model, run the command: python model.py which will generate the trained model and scaler files inside the models folder.

## Cloud Deployment
This application is cloud-ready and can be deployed on AWS EC2 by connecting to the instance, installing dependencies, and running the Flask application. The application can then be accessed using the EC2 public IP address.

## Skills Demonstrated
Machine Learning, Data Preprocessing, Feature Engineering, Model Training and Evaluation, Model Deployment, Flask Web Development, Cloud Deployment using AWS EC2, Full Stack Machine Learning Application Development

## Author
Aishwarya Boda
