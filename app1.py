import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('Loan_predict.pkl')


# Streamlit UI
st.title("Loan Prediction App")
st.write("Fill in the details below to predict if the loan will be approved or not.")

# User inputs
gender = st.selectbox("Gender", options=["Male", "Female"])
married = st.selectbox("Married", options=["Yes", "No"])
dependents = st.selectbox("Dependents", options=["0", "1", "2", "3+"])
education = st.selectbox("Education", options=["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", options=["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0.0, value=360.0)
credit_history = st.selectbox("Credit History", options=["Yes", "No"])
property_area = st.selectbox("Property Area", options=["Urban", "Rural", "Semiurban"])

# Encoding user inputs
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1.0 if credit_history == "Yes" else 0.0
property_area_mapping = {"Urban": 2, "Rural": 0, "Semiurban": 1}
property_area = property_area_mapping[property_area]

# Predict button
if st.button("Predict Loan Status"):
    # Prepare input data
    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_amount_term, credit_history, property_area]])
    
    # Scale input data
    
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
