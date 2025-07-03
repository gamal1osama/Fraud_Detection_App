import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('fraud_detection_model.pkl')

st.title("Fraud Detection System")

st.markdown("""
        This application detects fraudulent transactions using a machine learning model.
        Please enter the transaction details below.
            """)    


st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEPOSIT"]) 

amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)

oldbalanceOrg = st.number_input("Old Balance (Origin | Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Origin | Sender)", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance (Destination | Receiver)", min_value=0.0, value=5000.0)
newbalanceDest = st.number_input("New Balance (Destination | Receiver)", min_value=0.0, value=6000.0)

if st.button("Predict Fraud"):
    # Prepare the input data
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    # Display the result
    if prediction == 1:
        st.error("This transaction is likely fraudulent.")
    else:
        st.success("This transaction is likely legitimate.")