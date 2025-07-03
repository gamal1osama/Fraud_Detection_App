# 🛡️ Fraud Detection Using Machine Learning

A **Streamlit web application** for detecting fraudulent transactions using a machine learning model trained on real-world financial data.  

🎯 **Live Demo**: [fraud-detection-app1.streamlit.app](https://fraud-detection-app1.streamlit.app/)  

---

## 📊 Dataset

This project uses the [Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset) from Kaggle, which contains anonymized transaction data for training and evaluation.

---

## 🧠 Model Training

Explore the full workflow, including data exploration, feature engineering, and model training, in the Kaggle notebook:  
📓 [Fraud Detection ML (F1 Score: 95%)](https://www.kaggle.com/code/gamalosama/fraud-detection-ml-f1-score-95)

The trained model achieves **high accuracy and F1 score** for detecting fraudulent transactions.

---

## ✨ Features

✅ Predicts whether a financial transaction is **fraudulent** or **legitimate**  
✅ User-friendly **web interface** built with Streamlit  
✅ Accepts input for transaction details such as type, amount, and balances  
✅ Provides **instant predictions** and feedback  

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/fraud-detection-ml.git
cd fraud-detection-ml
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download the trained model
Ensure fraud_detection_model.pkl is placed in the project directory.

### 4️⃣ Launch the app
```bash
streamlit run fraud_detection.py
```
The app will open in your default browser at http://localhost:8501.
