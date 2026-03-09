import streamlit as st
import pickle

# Load model
model, vectorizer = pickle.load(open("model/spam_model.pkl", "rb"))

st.title("Spam Email Classifier")

st.write("Detect whether a message is spam or not using Machine Learning")

message = st.text_area("Enter Email Message")

if st.button("Predict"):

    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam")
