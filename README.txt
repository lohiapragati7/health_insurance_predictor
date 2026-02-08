Health Insurance Charges Estimator

A complete end-to-end Machine Learning + Data Science project that predicts medical insurance charges based on a person’s health, lifestyle, and financial details.

Built with Python, Scikit-learn, Streamlit, and deployed live on the cloud.

Live Demo: https://health-insurance-estimator.streamlit.app/

---

Project Highlights : 

1. End-to-End ML Pipeline  
2. Exploratory Data Analysis (EDA)  
3. Data Cleaning & Preprocessing    
4. Regression Model Training  
5. Interactive Streamlit Web App  

---

##  Problem Statement

Insurance charges vary depending on:

- Age
- BMI
- Smoking habits
- Hospital history
- Medical claims
- Salary
- Lifestyle activity

This project predicts expected insurance/medical charges using Machine Learning to help estimate future expenses.

---

Exploratory Data Analysis

Performed detailed data analysis using Matplotlib & Seaborn.

Data Cleaning : 

 - Handled missing/null values
 - Removed duplicates
 - Checked incorrect datatypes
 - Treated outliers using boxplots

Label Encoding for several Categorical features.

Visualizations Created :

- Category counts (sex, smoker, region)
- Distribution plots
- Correlation heatmap
- Pairplots
- Boxplots (outliers detection)
- Regression prediction vs actual plot

---

Key Insights from EDA :

## Correlation Heatmap
- Hospital expenditure strongly correlated with charges
- Annual salary positively related to claim amount
- Past hospitalizations significantly impact costs

## Smoker Analysis
- Smokers have significantly higher insurance charges

## Age Impact
- Charges increase with age

## Medical History
- More consultations & hospital visits → higher expenses

## Outliers
- High hospital expenditure & salary outliers detected
- Treated during preprocessing

---

Model Details :

Algorithm used : Linear Regression (Scikit-learn)

Target variable : Charges

Features :
1. Age
2. Sex
3. BMI
4. Children
5. Smoker
6. Claim Amount
7. Past Consultations
8. Number of Steps
9. Hospital Expenditure
10. Past Hospitalizations
11. Annual Salary
12. Region

 Performance :
- r2 Score : 97.88%
- high fit (based on regression plot)
- Low prediction error
- Actual vs Predicted values closely aligned

---

# Streamlit Web App

Users can:

✅ Enter personal details  
✅ Predict insurance cost instantly  
✅ Interactive UI  
✅ Real-time predictions  

---






