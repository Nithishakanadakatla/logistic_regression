<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title("🏦 Loan Prediction System (Complete ML Pipeline)")

# -------------------------------
# STEP 1: Upload Dataset
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Original Dataset")
    st.write(data.head())

    # -------------------------------
    # STEP 2: Missing Values
    # -------------------------------
    st.subheader("❗ Missing Values Before Handling")
    st.write(data.isnull().sum())

    # -------------------------------
    # STEP 3: Drop Loan_ID if exists
    # -------------------------------
    if 'Loan_ID' in data.columns:
        data = data.drop('Loan_ID', axis=1)

    # -------------------------------
    # STEP 4: Handle Missing Values
    # -------------------------------
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].mean())

    st.subheader("✅ Missing Values After Handling")
    st.write(data.isnull().sum())

    # -------------------------------
    # STEP 5: Encoding
    # -------------------------------
    data = pd.get_dummies(data, drop_first=True)

    st.subheader("🔄 After Encoding")
    st.write(data.head())

    # -------------------------------
    # STEP 6: Split Data
    # -------------------------------
    if 'Loan_Status_Y' not in data.columns:
        st.error("❌ Target column 'Loan_Status_Y' not found after encoding")
    else:
        X = data.drop('Loan_Status_Y', axis=1)
        y = data['Loan_Status_Y'].astype(int)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # -------------------------------
        # STEP 7: Train Model
        # -------------------------------
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # -------------------------------
        # STEP 8: Accuracy
        # -------------------------------
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        st.subheader("🎯 Model Accuracy")
        st.success(f"Accuracy: {acc:.2f}")

        # -------------------------------
        # STEP 9: User Input for Prediction
        # -------------------------------
        st.subheader("🧾 Enter Applicant Details")

        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        app_income = st.number_input("Applicant Income", min_value=0)
        coapp_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.number_input("Loan Amount Term", min_value=0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        # -------------------------------
        # STEP 10: Prediction
        # -------------------------------
        if st.button("Predict Loan Status"):

            input_data = pd.DataFrame({
                'ApplicantIncome': [app_income],
                'CoapplicantIncome': [coapp_income],
                'LoanAmount': [loan_amount],
                'Loan_Amount_Term': [loan_term],
                'Credit_History': [credit_history],
                'Gender_Male': [1 if gender == "Male" else 0],
                'Married_Yes': [1 if married == "Yes" else 0],
                'Dependents_1': [1 if dependents == "1" else 0],
                'Dependents_2': [1 if dependents == "2" else 0],
                'Dependents_3+': [1 if dependents == "3+" else 0],
                'Education_Not Graduate': [1 if education == "Not Graduate" else 0],
                'Self_Employed_Yes': [1 if self_employed == "Yes" else 0],
                'Property_Area_Semiurban': [1 if property_area == "Semiurban" else 0],
                'Property_Area_Urban': [1 if property_area == "Urban" else 0]
            })

            # Match training columns
            input_data = input_data.reindex(columns=X.columns, fill_value=0)

            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]

            # -------------------------------
            # Output
            # -------------------------------
            if prediction == 1:
                st.success(f"✅ Loan Approved (1)\nProbability: {probability:.2f}")
            else:
=======
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title("🏦 Loan Prediction System (Complete ML Pipeline)")

# -------------------------------
# STEP 1: Upload Dataset
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Original Dataset")
    st.write(data.head())

    # -------------------------------
    # STEP 2: Missing Values
    # -------------------------------
    st.subheader("❗ Missing Values Before Handling")
    st.write(data.isnull().sum())

    # -------------------------------
    # STEP 3: Drop Loan_ID if exists
    # -------------------------------
    if 'Loan_ID' in data.columns:
        data = data.drop('Loan_ID', axis=1)

    # -------------------------------
    # STEP 4: Handle Missing Values
    # -------------------------------
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].mean())

    st.subheader("✅ Missing Values After Handling")
    st.write(data.isnull().sum())

    # -------------------------------
    # STEP 5: Encoding
    # -------------------------------
    data = pd.get_dummies(data, drop_first=True)

    st.subheader("🔄 After Encoding")
    st.write(data.head())

    # -------------------------------
    # STEP 6: Split Data
    # -------------------------------
    if 'Loan_Status_Y' not in data.columns:
        st.error("❌ Target column 'Loan_Status_Y' not found after encoding")
    else:
        X = data.drop('Loan_Status_Y', axis=1)
        y = data['Loan_Status_Y'].astype(int)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # -------------------------------
        # STEP 7: Train Model
        # -------------------------------
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # -------------------------------
        # STEP 8: Accuracy
        # -------------------------------
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        st.subheader("🎯 Model Accuracy")
        st.success(f"Accuracy: {acc:.2f}")

        # -------------------------------
        # STEP 9: User Input for Prediction
        # -------------------------------
        st.subheader("🧾 Enter Applicant Details")

        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        app_income = st.number_input("Applicant Income", min_value=0)
        coapp_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.number_input("Loan Amount Term", min_value=0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        # -------------------------------
        # STEP 10: Prediction
        # -------------------------------
        if st.button("Predict Loan Status"):

            input_data = pd.DataFrame({
                'ApplicantIncome': [app_income],
                'CoapplicantIncome': [coapp_income],
                'LoanAmount': [loan_amount],
                'Loan_Amount_Term': [loan_term],
                'Credit_History': [credit_history],
                'Gender_Male': [1 if gender == "Male" else 0],
                'Married_Yes': [1 if married == "Yes" else 0],
                'Dependents_1': [1 if dependents == "1" else 0],
                'Dependents_2': [1 if dependents == "2" else 0],
                'Dependents_3+': [1 if dependents == "3+" else 0],
                'Education_Not Graduate': [1 if education == "Not Graduate" else 0],
                'Self_Employed_Yes': [1 if self_employed == "Yes" else 0],
                'Property_Area_Semiurban': [1 if property_area == "Semiurban" else 0],
                'Property_Area_Urban': [1 if property_area == "Urban" else 0]
            })

            # Match training columns
            input_data = input_data.reindex(columns=X.columns, fill_value=0)

            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]

            # -------------------------------
            # Output
            # -------------------------------
            if prediction == 1:
                st.success(f"✅ Loan Approved (1)\nProbability: {probability:.2f}")
            else:
>>>>>>> 187d65c (Initial commit: logistic regression app and dataset)
                st.error(f"❌ Loan Rejected (0)\nProbability: {probability:.2f}")