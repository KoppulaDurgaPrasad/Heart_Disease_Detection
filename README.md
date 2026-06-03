# ❤️ Heart Disease Prediction System

A Machine Learning web application that predicts the likelihood of heart disease using patient health data. The project follows a complete machine learning pipeline including **Data Cleaning**, **Exploratory Data Analysis (EDA)**, **Feature Engineering**, **Model Training**, **Model Evaluation**, and **Deployment** using Streamlit.

## 🚀 Live Demo

🔗 **Try the Application**

https://koppuladurgaprasad-heart-disease-detection-heart-e9d2ig.streamlit.app/

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help patients seek timely medical attention and reduce health risks.

This project uses machine learning techniques to analyze patient health attributes and predict whether a patient is at high risk or low risk of heart disease.

---

## ✨ Features

* Real-time heart disease prediction
* Interactive Streamlit web interface
* Patient health summary dashboard
* Risk probability visualization
* Machine Learning based predictions
* Responsive and user-friendly design
* Cloud deployment using Streamlit Community Cloud

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Joblib

### Development Tools

* Jupyter Notebook
* VS Code
* Git & GitHub

---

## 📊 Dataset

Dataset Used: **Heart Disease Dataset (`heart.csv`)**

The dataset contains patient health information including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope
* Heart Disease Target Variable

---

## 🧹 Data Preprocessing

Before training the machine learning models, the dataset was cleaned and prepared.

### Data Cleaning

The following steps were performed:

* Checked for missing values
* Verified data types
* Removed duplicate records
* Validated categorical and numerical features
* Prepared data for machine learning training

### Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and identify meaningful patterns.

Analysis included:

* Age distribution analysis
* Gender-wise heart disease distribution
* Chest pain type analysis
* Cholesterol level analysis
* Blood pressure analysis
* Heart disease occurrence patterns
* Correlation analysis among features

### Feature Engineering

To improve model performance:

* Categorical variables were converted using One-Hot Encoding
* Numerical features were standardized using StandardScaler
* Features were aligned for training and inference consistency
* Dataset was split into training and testing sets

---

## 🤖 Machine Learning Models Evaluated

Several machine learning algorithms were trained and compared.

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression | **86.41%** |
| KNN                 |     85.33% |
| Naive Bayes         |     85.33% |
| SVM (RBF Kernel)    |     84.78% |
| Decision Tree       |     79.35% |

---

## 🏆 Model Selection

After evaluating multiple machine learning algorithms, **Logistic Regression** was selected as the final model because it achieved the highest accuracy.

### Selection Process

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Scaling
5. Model Training
6. Model Evaluation
7. Performance Comparison
8. Best Model Selection

### Final Selected Model

**Logistic Regression**

**Accuracy:** 86.41%

Reasons for Selection:

* Highest accuracy among tested models
* Fast prediction speed
* Good generalization capability
* Easy interpretability
* Well suited for binary classification problems

---

## 📈 Model Performance

### Final Model

| Metric       | Value                 |
| ------------ | --------------------- |
| Algorithm    | Logistic Regression   |
| Accuracy     | 86.41%                |
| Problem Type | Binary Classification |

### Prediction Classes

| Output | Interpretation             |
| ------ | -------------------------- |
| 0      | Low Risk of Heart Disease  |
| 1      | High Risk of Heart Disease |

---

## 📋 Features Used for Prediction

The deployed model uses the following patient attributes:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak (ST Depression)
* ST Slope

---

## 📂 Project Structure

```text
Heart_Disease_Detection/
│
├── Heart.py
├── Logistic_Regression.pkl
├── scaler.pkl
├── columns.pkl
├── heart.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/KoppulaDurgaPrasad/Heart_Disease_Detection.git
cd Heart_Disease_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run Heart.py
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

https://koppuladurgaprasad-heart-disease-detection-heart-e9d2ig.streamlit.app/

---

## 📸 Application Workflow

1. Enter patient health information
2. Click **Predict Heart Disease Risk**
3. Model processes the input data
4. Prediction is generated
5. Risk probability is displayed
6. User receives a final risk assessment


---

## 👨‍💻 Developer

### Durga Prasad Koppula

GitHub:
https://github.com/KoppulaDurgaPrasad

---

## ⭐ Support

If you found this project useful, please consider giving the repository a ⭐ on GitHub.

Contributions, suggestions, and feedback are always welcome.

---

### Made with ❤️ using Python, Machine Learning, and Streamlit
