# 🐱🐶 Cat vs Dog Image Classifier

An end-to-end Machine Learning web application that classifies images as cats or dogs using a Support Vector Machine (SVM) model. The application is deployed using Streamlit and provides real-time predictions through an interactive and user-friendly interface.

---

## 📖 Overview

This project demonstrates the complete machine learning lifecycle — from data preprocessing and model training to deployment. Users can upload an image, and the system predicts whether it is a cat or a dog in real time.

---

## 🚀 Features

* 📤 Upload image for prediction
* ⚡ Real-time classification
* 🧠 Machine learning model (SVM)
* 🖥️ Interactive UI using Streamlit
* 🔄 End-to-end ML workflow

---

## 🧠 Model & Approach

* **Algorithm:** Support Vector Machine (SVM)
* **Library:** scikit-learn
* **Type:** Binary Classification

### 📊 Data Preprocessing

* Resized images to **64×64 pixels**
* Converted images to **grayscale**
* Flattened images into feature vectors

---

## ⚙️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:** NumPy, scikit-learn, Pillow (PIL), OpenCV (optional)

---

## 📁 Project Structure

cat-dog-classifier/
│── app.py               # Streamlit app
│── model.pkl            # Trained model
│── requirements.txt     # Dependencies
│── runtime.txt          # Python version
│── README.md            # Documentation

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

git clone [https://github.com/BalajiP73/Image_Preprocessing.git]
cd Image_Preprocessing

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run Application

streamlit run app.py

---

## 🌐 Deployment

Deployed using Streamlit Cloud for easy access and real-time usage.

---

## 📸 Demo

<img width="820" height="856" alt="image" src="https://github.com/user-attachments/assets/35f1bfb5-3bbf-4453-99c8-e1243056a832" />

<img width="751" height="818" alt="image" src="https://github.com/user-attachments/assets/d1fa440f-c5fa-4c35-9c64-957096eaa08f" />

---

## 📈 Model Performance

* Achieved ~80% accuracy on test dataset *(update this if available)*

---

## 📊 Future Improvements

* Replace SVM with Deep Learning (CNN)
* Add prediction confidence score
* Improve UI/UX design
* Deploy using Docker or cloud platforms

---

## 📌 Key Highlights

* Built a complete ML pipeline from preprocessing to deployment
* Integrated trained model into a web application
* Enabled real-time predictions with a simple UI
* Demonstrates practical machine learning deployment skills

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
