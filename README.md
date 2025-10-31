🐾 Cat vs Dog Image Classifier

An elegant and interactive AI-powered image classifier built using TensorFlow and Streamlit, capable of distinguishing between 🐱 cats and 🐶 dogs.

This version features a modern animated UI, smooth prediction transitions, and a clean, responsive layout — perfect for demos, learning, or deployment!

🌟 Features

🧠 Deep Learning Model trained using TensorFlow & Keras

📸 Upload any image to get instant predictions

🌈 Animated gradient background and glowing effects

🎞️ Smooth progress animations and result transitions

🎨 Beautiful, modern Streamlit UI with snow and balloons

💾 Local model loading — no external API required

📂 Project Structure
image_classifier_project/
│
├── data/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   └── test/
│       ├── cats/
│       └── dogs/
│
├── models/
│   └── cat_dog_model.h5
│
├── main.py          # Script to train and predict from CLI
├── app.py           # Streamlit web app (UI)
├── requirements.txt # Dependencies
└── README.md

🛠️ Installation & Setup
1️⃣ Clone or Download the Project
git clone https://github.com/yourusername/cat-dog-classifier.git
cd cat-dog-classifier

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model (if not trained yet)

Make sure your dataset is inside data/train/ and data/test/ folders.
Then run:

python main.py --train --epochs 5


This will save your trained model to models/cat_dog_model.h5.

4️⃣ Run the Web App
streamlit run app.py


Then open the link (usually http://localhost:8501
) in your browser.

📸 How It Works

Upload an image (JPEG/PNG).

The model resizes it to 64x64 and runs inference.

The prediction (🐱 Cat or 🐶 Dog) is displayed with confidence %.

Smooth animations and effects make it visually appealing!

📊 Example Output

Input:
📷 An image of a cat

Output:

✅ Prediction: Cat
💯 Confidence: 95.83%


🐾 Balloons float for Cats 🎈
❄️ Snow effect for Dogs ☃️

⚙️ Model Details

Framework: TensorFlow / Keras

Architecture: Simple CNN with Conv2D → MaxPool → Dense layers

Input size: 64x64 pixels

Output: Binary classification (Cat = 0, Dog = 1)

💡 Future Enhancements

🔹 Add support for more animal classes

🔹 Include Grad-CAM visualization

🔹 Deploy to Streamlit Cloud or Hugging Face Spaces

❤️ Credits

Developed with 🧠 TensorFlow, 💻 Python, and ✨ Streamlit.
Designed and built by [Your Name].
