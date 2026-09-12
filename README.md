# Multilingual Fake News Detection (English & Kannada)

An end-to-end machine learning pipeline and web application designed to classify text as **Real (0)** or **Fake (1)**. This project focuses on handling English, Kannada, and code-mixed inputs without text rendering issues (UTF-8 encoding) using a fine-tuned **XLM-RoBERTa** model.

## 🚀 Tech Stack

*   **Model:** `xlm-roberta-base` (270M parameters)
*   **Machine Learning:** PyTorch, Hugging Face Transformers, Scikit-Learn
*   **Backend API:** FastAPI, Uvicorn
*   **Frontend:** React.js
*   **Database:** MongoDB (Prediction logging & analytics)

## 📊 Model Performance Targets

The model is fine-tuned to achieve high accuracy across both high-resource and low-resource languages:
*   **Overall Accuracy:** > 91%
*   **English Accuracy:** > 93%
*   **Kannada Accuracy:** > 85%

*Hyperparameters used for training: Batch Size = 8, Learning Rate = 2e-5, Epochs = 3-4, Max Length = 128-256.*

## 📁 Project Structure

```text
├── data/                  # Raw and processed datasets (UTF-8)
├── model_training/        # PyTorch/HF training scripts and notebooks
├── backend/               # FastAPI application and routing
│   ├── app.py             # Main API wrapper
│   └── database.py        # MongoDB connection handler
├── frontend/              # React application
│   ├── src/               
│   └── package.json       
├── requirements.txt       # Python dependencies
└── README.md
