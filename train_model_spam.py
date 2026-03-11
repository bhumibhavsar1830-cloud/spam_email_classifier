import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ── Fix paths ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(BASE_DIR, "DataSet", "Spam.csv")
model_dir  = os.path.join(BASE_DIR, "model")
model_path = os.path.join(model_dir, "spam_model.pkl")

# Create model folder if not exists
os.makedirs(model_dir, exist_ok=True)

# Load dataset
data = pd.read_csv(data_path, encoding='latin-1')

# Keep only first 2 columns
data = data.iloc[:, :2]
data.columns = ["label", "message"]

# Convert labels
data["label"] = data["label"].map({"ham": 0, "spam": 1})
data.dropna(inplace=True)

# Features and target
X = data["message"]
y = data["label"]

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Save model
pickle.dump((model, vectorizer), open(model_path, "wb"))
print("Model saved at:", model_path)
