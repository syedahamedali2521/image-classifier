# 🐶🐱 Cat vs Dog Image Classifier

A beautiful and interactive **Deep Learning web app** built with **TensorFlow** and **Streamlit**, designed to classify images as **Cat** or **Dog** with smooth animations and a clean modern UI.

---

## 🚀 Features

- 🧠 **CNN-based Deep Learning Model** trained on cats and dogs images  
- 🖼️ **Upload any image** to classify instantly  
- 💫 **Smooth, animated, and responsive UI** built using Streamlit  
- 💾 **Pre-trained model included** (`models/cat_dog_model.h5`)  
- ☁️ **Deployable on Streamlit Cloud or Hugging Face Spaces**

---

## 🗂️ Project Structure

image_classifier_project/
│
├── app.py # Streamlit web app
├── main.py # Model training and prediction script
├── requirements.txt # Dependencies
├── models/
│ └── cat_dog_model.h5 # Pre-trained Keras model
├── data/
│ ├── train/
│ │ ├── cats/
│ │ └── dogs/
│ └── test/
│ ├── cats/
│ └── dogs/
└── README.md

yaml
Copy code

---

## 🧩 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/syedahamedali2521/image-classifier.git
cd image-classifier
2️⃣ Install Dependencies
Make sure you have Python 3.9–3.11 (recommended).

bash
Copy code
pip install -r requirements.txt
3️⃣ Train the Model (optional)
If you want to retrain:

bash
Copy code
python main.py --train --epochs 5
4️⃣ Run the Streamlit App
bash
Copy code
streamlit run app.py
🌐 Deployment (Streamlit Cloud)
Push your code to GitHub

Go to Streamlit Cloud

Create a new app → Connect your GitHub repo

Set the main file path as:

bash
Copy code
image_classifier_project/app.py
Deploy 🚀

🖼️ Example
Image	Prediction	Confidence
🐱 cat1.jpeg	🐱 Cat	97%
🐶 dog1.jpeg	🐶 Dog	95%

📦 Requirements
makefile
Copy code
tensorflow==2.20.0
numpy
pillow
streamlit
❤️ Credits
Created by Syed Ahamed Ali
Built with TensorFlow, Keras, and Streamlit

📜 License
MIT License © 2025 Syed Ahamed Ali