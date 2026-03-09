# Spam Email Classifier

A Machine Learning based web application that detects whether an email message is spam or legitimate using Natural Language Processing (NLP).

## Problem Statement
Spam emails are a major issue in digital communication. They waste user time, spread phishing attacks, and reduce productivity. Detecting spam automatically can help protect users and improve email filtering systems.

## Proposed Solution
This project uses NLP techniques and a Naive Bayes machine learning model to classify email messages as spam or not spam. The text is converted into numerical features using TF-IDF vectorization and then classified using a trained model.

## Features
- Spam email detection using Machine Learning
- NLP based text processing
- Interactive web interface using Streamlit
- Real-time message prediction

## Tech Stack
- Python
- Scikit-learn
- Pandas
- Streamlit
- Natural Language Processing (NLP)

## Model Used
Multinomial Naive Bayes Classifier

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Future Improvements
- Deep learning based spam detection
- Email attachment scanning
- Phishing URL detection
- Real-time email integration
