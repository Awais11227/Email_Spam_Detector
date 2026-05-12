# **Email Spam Detector**

An intelligent Machine Learning based Email Spam Detection system that classifies emails as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and supervised learning algorithms.

Built with Python and designed as an end-to-end beginner-to-intermediate ML project for practical learning and portfolio showcasing.

---

##  Project Overview

This project uses Machine Learning and text preprocessing techniques to automatically detect spam emails. The system cleans and vectorizes email text data, trains a classification model, evaluates performance, and predicts whether an incoming email is spam or legitimate.

The project demonstrates:

- Data Cleaning
- NLP Preprocessing
- Feature Extraction using TF-IDF
- Model Training
- Model Evaluation
- Saving & Loading ML Models
- Real-world Email Prediction

---

# Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- NLTK
- TF-IDF Vectorization
- Machine Learning

---

# 📂 Project Structure

```bash
Email_Spam_Detector/
│
├── clean.py             
├── load_data.py          
├── vectorize.py          
├── train.py              
├── evaluate.py           
├── save.py                
├── email_bot.py        
│
├── Screenshot 2026-05-11 120738.png
├── Screenshot 2026-05-11 120806.png
│
└── README.md
```

---

# Features

✅ Spam vs Ham Classification  
✅ NLP Text Cleaning  
✅ TF-IDF Vectorization  
✅ ML Model Training  
✅ Accuracy Evaluation  
✅ Model Persistence  
✅ Custom Email Prediction  

---

#  Machine Learning Workflow

## 1️⃣ Load Dataset

The dataset is loaded and prepared for preprocessing.

```python
python load_data.py
```

---

## 2️⃣ Clean Text Data

Preprocessing includes:

- Lowercasing
- Removing punctuation
- Removing stopwords
- Tokenization

```python
python clean.py
```

---

## 3️⃣ Vectorize Text

TF-IDF converts textual email data into numerical vectors.

```python
python vectorize.py
```

---

## 4️⃣ Train the Model

Train the spam classification model.

```python
python train.py
```

---

## 5️⃣ Evaluate Performance

Check model accuracy and evaluation metrics.

```python
python evaluate.py
```

---

## 6️⃣ Run Email Prediction Bot

Predict whether a custom email is spam or not.

```python
python email_bot.py
```



---

#  ML Concepts Used

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Text Classification
- Supervised Machine Learning
- Data Preprocessing
- Feature Engineering

---

#  Future Improvements

- Add Flask/Django Web Interface
- Deploy on Streamlit
- Add Deep Learning Models
- Real-time Email API Integration
- Improve Accuracy with Hyperparameter Tuning

---

#  Learning Outcomes

Through this project, I learned:

- End-to-end ML workflow
- NLP preprocessing techniques
- Text vectorization methods
- Training and evaluating ML models
- Building real-world AI applications

---

# 👨‍💻 Author

## Awais Manzoor

- Data Analyst
- Machine Learning Enthusiast
- Python & SQL Developer

GitHub: https://github.com/Awais11227

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share feedback  

---

# 📜 License

This project is open-source and available under the MIT License.# Email_Spam_Detector
