import os
import pickle
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ── Fix paths ─────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "spam_model.pkl")
data_path  = os.path.join(BASE_DIR, "DataSet", "Spam.csv")

# ── Auto train if model not found ─────────────────────────
def train_and_save():
    data = pd.read_csv(data_path, encoding='latin-1')
    data = data.iloc[:, :2]
    data.columns = ["label", "message"]
    data["label"] = data["label"].map({"ham": 0, "spam": 1})
    data.dropna(inplace=True)

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(data["message"])
    y = data["label"]

    model = MultinomialNB()
    model.fit(X, y)

    os.makedirs(os.path.join(BASE_DIR, "model"), exist_ok=True)
    pickle.dump((model, vectorizer), open(model_path, "wb"))
    return model, vectorizer

# ── Load model ────────────────────────────────────────────
if os.path.exists(model_path):
    model, vectorizer = pickle.load(open(model_path, "rb"))
else:
    model, vectorizer = train_and_save()

# ── UI ────────────────────────────────────────────────────
st.set_page_config(page_title="Spam Email Classifier", page_icon="📧", layout="centered")

st.title("📧 Spam Email Classifier")
st.write("Detect whether a message is **Spam** or **Legitimate** using Machine Learning & NLP")

st.markdown("---")

message = st.text_area("Enter Email Message", height=150, placeholder="Type or paste your email message here...")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message!")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]
        if prediction == 1:
            st.error("🚨 SPAM Message Detected!")
        else:
            st.success("✅ Legitimate Message — Not Spam!")

st.markdown("---")
st.caption("Built with Python | Scikit-learn | NLP | Streamlit")
