import streamlit as st
import cv2
import numpy as np
import pickle
from PIL import Image

# -------------------------
# Load trained model
# -------------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------------
# Title
# -------------------------
st.title("🐶🐱 Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it's a Cat or Dog.")

# -------------------------
# File Upload
# -------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img = np.array(image)
    img = cv2.resize(img, (64, 64))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Flatten image (same as training)
    img = img.flatten().reshape(1, -1)

    # Prediction
    prediction = model.predict(img)

    # Output
    if prediction[0] == 0:
        st.success("Prediction: 🐱 Cat")
    else:
        st.success("Prediction: 🐶 Dog")
