import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, UnidentifiedImageError
import time
import io

# ================================
# 🎨 Page Configuration
# ================================
st.set_page_config(page_title="🐱🐶 Cat vs Dog Classifier", page_icon="🐾", layout="centered")

# ================================
# 🌈 Custom CSS Styling
# ================================
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        animation: gradientShift 8s ease infinite;
        background-size: 400% 400%;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    h1 {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        color: white;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }

    .uploadedFile {
        border-radius: 15px;
        background-color: rgba(255,255,255,0.2);
        padding: 1rem;
        margin-top: 1rem;
    }

    .img-container {
        display: flex;
        justify-content: center;
    }

    img {
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        transition: transform 0.4s ease-in-out;
    }

    img:hover {
        transform: scale(1.05);
    }

    .result {
        text-align: center;
        font-size: 1.6rem;
        font-weight: bold;
        color: #fff;
        text-shadow: 1px 1px 8px rgba(0,0,0,0.5);
        margin-top: 15px;
    }

    footer {
        text-align: center;
        color: rgba(255,255,255,0.8);
        font-size: 0.9rem;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# ================================
# 🧠 Load Model
# ================================
MODEL_PATH = "models/cat_dog_model.h5"

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# ================================
# 🔮 Prediction Function
# ================================
def predict_image(image):
    img = image.resize((64, 64))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    class_names = ["Cat", "Dog"]
    predicted_class = class_names[int(predictions[0][0] > 0.5)]
    confidence = predictions[0][0] if predicted_class == "Dog" else 1 - predictions[0][0]
    return predicted_class, float(confidence)

# ================================
# 🖼️ Streamlit App Layout
# ================================
st.title("🐾 Cat vs Dog Classifier")

uploaded_file = st.file_uploader("📸 Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Read and open image safely
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        st.markdown('<div class="uploadedFile">', unsafe_allow_html=True)
        st.markdown('<div class="img-container">', unsafe_allow_html=True)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Animation before prediction
        with st.spinner("✨ Analyzing your image..."):
            progress_text = "🔍 Processing..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.02)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.5)

            predicted_class, confidence = predict_image(image)
            my_bar.empty()

        # Result Display with Animation
        st.markdown(f"""
            <div class="result">
                ✅ Prediction: <b>{predicted_class}</b><br>
                💯 Confidence: <b>{confidence * 100:.2f}%</b>
            </div>
        """, unsafe_allow_html=True)

        if predicted_class == "Cat":
            st.balloons()
        else:
            st.snow()

        st.markdown('</div>', unsafe_allow_html=True)

    except UnidentifiedImageError:
        st.error("⚠️ The uploaded file is not a valid image. Please upload a JPG or PNG.")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")

else:
    st.info("👆 Upload an image to get started.")

# ================================
# 🌟 Footer
# ================================
st.markdown("""
    <footer>
        Made with ❤️ by <b>Syed Ahamed Ali</b>
    </footer>
""", unsafe_allow_html=True)


