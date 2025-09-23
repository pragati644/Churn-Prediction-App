# churn_app.py
import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("best_xgb_model.pkl")

st.title("Customer Churn Prediction App")
st.write("Fill in customer details to check if they are likely to churn.")

# --- User Inputs ---
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=500.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=800.0)

gender = st.selectbox("Gender", ["Male", "Female"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

# --- Prediction Button ---
if st.button("Predict Churn"):
    # Create dataframe from inputs
    input_data = pd.DataFrame({
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'gender': [gender],
        'Partner': [partner],
        'Dependents': [dependents],
        'PhoneService': [phone_service],
        'InternetService': [internet_service],
        'Contract': [contract],
        'PaymentMethod': [payment_method]
    })

    # One-hot encode inputs to match training features
    input_data = pd.get_dummies(input_data)

    # Align with model training columns
    model_features = model.get_booster().feature_names
    input_data = input_data.reindex(columns=model_features, fill_value=0)

    # Predict churn
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"⚠️ Customer is likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer is not likely to churn (Probability: {probability:.2f})")
