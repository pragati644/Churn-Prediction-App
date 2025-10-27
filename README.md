# Churn Prediction Project 📊

## Overview

This project is a **Customer Churn Prediction** application designed to predict whether a customer is likely to churn (leave) a service. It includes exploratory data analysis (EDA), model training, and a Streamlit app for interactive predictions.

The project uses machine learning techniques, including **XGBoost**, to deliver accurate predictions. The Streamlit app allows users to input customer details and see the churn prediction in real-time.

---

## Folder Structure

```
Churn-Prediction-App/
│
├── app/                     # Streamlit scripts
│   └── churn_NEWFORSTREAM.py
├── notebooks/               # Jupyter notebooks
│   └── churn.ipynb
├── models/                  # Saved models
│   └── best_xgb_model.pkl
├── data/                    # Dataset
│   └── customer_churn.xlsx
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitattributes           # Git config
```

---

## Dataset

* **File:** `customer_churn.xlsx`
* Contains customer data with features relevant for predicting churn.
* Columns include demographic info, account details, usage metrics, etc.
* Make sure to place the dataset in the `data/` folder for the app to work correctly.

---

## Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, streamlit
* **Machine Learning:** XGBoost Classifier (best performing model)
* **Frontend:** Streamlit for interactive app
* **Version Control:** Git & GitHub

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
```

2. Navigate to the project folder:

```bash
cd Churn-Prediction-App
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

1. Make sure the dataset is in the `data/` folder.
2. Start the Streamlit app:

```bash
streamlit run app/churn_NEWFORSTREAM.py
```

3. The app will open in your default browser.
4. Input customer details to see **predicted churn**.

---

## Results

* The trained **XGBoost model** predicts churn with high accuracy.
* The app displays results in a **user-friendly interface**.
* Future improvements can include **real-time database integration** and **multi-model comparison**.

---

## Optional: Screenshots

*(Add screenshots of the Streamlit app for visual appeal)*

---

## Notes

* Avoid pushing large files frequently.
* Add `.gitignore` to ignore:

```
__pycache__/
*.pyc
*.pkl
*.env
*.ipynb_checkpoints
```

* Rename files for consistency and avoid spaces: e.g., `customer churn (1).xlsx` → `customer_churn.xlsx`

---


This README makes your repo **professional and recruiter-ready**.
