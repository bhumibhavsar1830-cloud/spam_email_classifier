<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6&height=180&section=header&text=Spam%20Email%20Classifier&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Machine%20Learning%20%7C%20NLP%20%7C%20Streamlit&descAlignY=58&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![NLP](https://img.shields.io/badge/NLP-TF--IDF-8E44AD?style=for-the-badge&logo=google&logoColor=white)]()
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**An AI-powered Spam Email Detector using NLP and Naive Bayes — classifies emails as Spam or Legitimate in real-time via an interactive Streamlit web app.**

</div>

---

## 📌 Overview

Spam emails are a major threat in digital communication — they waste time, spread phishing attacks, and reduce productivity. This project uses **Natural Language Processing (NLP)** and **Multinomial Naive Bayes** to automatically detect spam emails with high accuracy.

The system converts email text into numerical features using **TF-IDF Vectorization** and classifies them as **Spam** or **Not Spam** — all through an interactive Streamlit dashboard.

---

## 🚨 Problem

- ❌ Billions of spam emails sent daily worldwide
- ❌ Phishing attacks via email cause financial losses
- ❌ Manual spam filtering is slow and inefficient
- ❌ Existing filters miss context-aware spam messages

---

## ✅ Solution

| Feature | Description |
|---------|-------------|
| 🧠 **ML Classification** | Multinomial Naive Bayes trained on real email data |
| 📝 **NLP Processing** | TF-IDF Vectorization converts text to features |
| ⚡ **Real-time Detection** | Instant spam prediction on any input message |
| 🌐 **Web Interface** | Interactive Streamlit app — no coding needed |
| 📊 **Visual Feedback** | Clear Spam / Not Spam result with confidence |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| ML Model | Multinomial Naive Bayes (Scikit-learn) |
| NLP | TF-IDF Vectorizer |
| Web App | Streamlit |
| Data Processing | Pandas, NumPy |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
spam_email_classifier/
│
├── app.py               ← Streamlit web app (main)
├── train_model.py       ← Model training script
│
├── DataSet/             ← Email dataset folder
│
├── requirements.txt     ← Python dependencies
├── LICENSE
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/bhumibhavsar1830-cloud/spam_email_classifier.git
cd spam_email_classifier
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Train the model**
```bash
python train_model.py
```

**4. Run the app**
```bash
streamlit run app.py
```

**5. Open in browser**
```
http://localhost:8501
```

---

## 🧠 How It Works

```
Email Text Input
      ↓
Text Preprocessing (lowercase, remove punctuation)
      ↓
TF-IDF Vectorization (converts text → numbers)
      ↓
Multinomial Naive Bayes Model
      ↓
Output: SPAM ❌  or  NOT SPAM ✅
```

---

## 📈 Model Details

- **Algorithm** — Multinomial Naive Bayes Classifier
- **Feature Extraction** — TF-IDF Vectorizer
- **Input** — Raw email/message text
- **Output** — Spam or Legitimate (Ham)
- **Training Data** — Real-world email dataset

---

## 🔮 Future Improvements

- [ ] Deep Learning based spam detection (LSTM/BERT)
- [ ] Email attachment scanning
- [ ] Phishing URL detection
- [ ] Real-time Gmail/Outlook integration
- [ ] Multi-language spam detection

---

## 📄 License

MIT License — open source and free to use.

---

<div align="center">

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Naive%20Bayes-8E44AD?style=for-the-badge)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6&height=120&section=footer&text=Stop%20Spam%20with%20AI&fontSize=24&fontColor=ffffff&fontAlignY=65&animation=fadeIn" width="100%"/>

</div>
