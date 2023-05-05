#http://127.0.0.1:8000/docs#/default(paste the url in to any web)

#https://openphish.com/(fake website list)

import streamlit as st
import joblib
import requests

# Download and save the model
url = 'https://raw.githubusercontent.com/shivkumarg3/FakeWebsiteDetection/main/phishing.pkl'
response = requests.get(url)

with open('phishing.pkl', 'wb') as f:
    f.write(response.content)

# Load the model
phish_model_ls = joblib.load('phishing.pkl')

# Streamlit UI
st.title("Fake Website Detection")
feature = st.text_input("Enter the website URL:")

if st.button("Predict"):
    if feature:
        X_predict = [feature]
        y_Predict = phish_model_ls.predict(X_predict)
        if y_Predict[0] == 'bad':
            st.warning("This is a Phishing Site(fake website)")
        else:
            st.success("This is not a Phishing Site(good website)")
    else:
        st.error("Please enter a valid URL")
