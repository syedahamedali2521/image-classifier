import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# 🎨 Page Configuration
st.set_page_config(
    page_title="🐶🐱 Cat & Dog Image Classifier",
    page_icon="🐾",
    layout="wide",
)

# 🌈 Custom CSS for Beautiful UI
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #89f7fe, #66a6ff);
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: white;
}
div.stButton > button:first-child {
    background-color: #4A90E2;
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background-color: #357ABD;
    transform: scale(1.05);
}
.uploadedImage {
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 🧠 Model Loading
MODEL_PATH = "models/cat_dog_model.h5"

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

model = load_model()

# 🏷️ Class labels
CLASS_NAMES = ['Cat', 'Dog']

# 🧩 App Header
st.markdown("<h1>🐾 Cat vs Dog Classifier</h1>", unsafe_allow_html=True)
st.write("Upload an image below and let the AI tell you if it’s a **Cat** or a **Dog!**")

# 📤 File Upload Section
uploaded_file = st.file_uploader("📸 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Open and display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Image", use_container_width=True)

        # Convert and preprocess
        img = image.resize((150, 150))
        img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

        # Prediction button
        if st.button("🔍 Predict"):
            with st.spinner("Analyzing image... 🧠"):
                prediction = model.predict(img_array)
                predicted_class = CLASS_NAMES[int(prediction[0][0] > 0.5)]
                confidence = float(prediction[0][0]) if predicted_class == "Dog" else 1 - float(prediction[0][0])

            st.success(f"**Prediction:** {predicted_class} 🐾")
            st.progress(confidence)
            st.balloons()
    except Exception as e:
        st.error(f"⚠️ Error loading image: {e}")
else:
    st.info("👆 Upload a cat or dog image to begin.")            

# ✨ Footer
st.markdown(
    "<p style='text-align:center; color:white;'>Made by ❤️ Syed Ahamed Ali</p>",
    unsafe_allow_html=True
)






