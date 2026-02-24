# 💧 Water Potability Prediction Web App

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-MachineLearning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-black?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-NumericalComputing-blue?logo=numpy)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Classification](https://img.shields.io/badge/Model-Classification-yellow)
![Deployment](https://img.shields.io/badge/Deployment-StreamlitCloud-success)

A smart machine learning–based web application that predicts whether water is safe for drinking based on important chemical parameters.
Built using Python, Scikit-learn, and Streamlit, and deployed for public use online!

## 🔗 Live Demo

Try the deployed web app here: https://water-portability-prediction-by-saikat-pradhan.streamlit.app/

## 🚀 Project Overview

This project demonstrates how machine learning can analyze water quality and determine potability.
A classification model predicts whether water is good or poor using user inputs, and the result is shown instantly in a clean web interface.

## Input Fields:

- pH
- Hardness
- Chloramines
- Organic Carbon
- Turbidity

## Output:

- ✅ Good Water Quality
- ❌ Poor Water Quality

## 🧠 Technologies Used

- Python 🐍
- Streamlit 🌐
- Pandas 📊
- NumPy 📐
- Scikit-learn 🤖
- Pickle 📦

## ⚙️ Setup Guide (Run Locally)
1️⃣ Clone the Repository

```
git clone https://github.com/Saikat-Pradhan/Water-Portability-Prediction.git
cd Water-Portability-Prediction
```

2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

3️⃣ Run the App

```
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

## 📊 Dataset

The dataset (water_potability.csv) includes:

- ph
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic_carbon
- Trihalomethanes
- Turbidity
- Potability

This data trains the model to understand water quality patterns.

## 🏗️ Model Training

Model development happens in:

Water_Quality_Analysis.ipynb


It includes:

- Data preprocessing
- Missing value handling
- Feature selection
- Classification model training
- Model evaluation
- Saving the model with Pickle

## 🧠 How the App Works

- User enters water quality parameters
- Inputs go through the trained ML model
- Model predicts potability status
- Result displays instantly on the UI

⭐ Support

If you like this project, don’t forget to give it a star ⭐ on GitHub!
It motivates me to build more useful ML projects 🚀
