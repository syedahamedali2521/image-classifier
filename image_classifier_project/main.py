import os
import argparse
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

# ==========================================================
# 🏗️ MODEL CREATION FUNCTION
# ==========================================================
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D(pool_size=(2, 2)),

        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),

        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model


# ==========================================================
# 🎓 TRAINING FUNCTION
# ==========================================================
def train_model(epochs=5):
    train_dir = "data/train"
    test_dir = "data/test"

    if not os.path.exists(train_dir) or not os.path.exists(test_dir):
        print("❌ Training or testing directories not found. Please ensure 'data/train' and 'data/test' exist.")
        return

    # Image generators
    train_gen = ImageDataGenerator(rescale=1.0/255)
    test_gen = ImageDataGenerator(rescale=1.0/255)

    train_data = train_gen.flow_from_directory(
        train_dir, target_size=(64, 64), batch_size=8, class_mode='binary'
    )
    test_data = test_gen.flow_from_directory(
        test_dir, target_size=(64, 64), batch_size=8, class_mode='binary'
    )

    # Build and train the model
    model = build_model()
    model.fit(train_data, validation_data=test_data, epochs=epochs)

    # Save model
    os.makedirs("models", exist_ok=True)
    model.save("models/cat_dog_model.h5")
    print("✅ Model training completed and saved as 'models/cat_dog_model.h5'!")


# ==========================================================
# 🔍 PREDICTION FUNCTION
# ==========================================================
def predict_image(model_path, image_path, class_labels=['cat', 'dog']):
    if not os.path.exists(model_path):
        print("❌ Model file not found. Train the model first using --train.")
        return
    if not os.path.exists(image_path):
        print("❌ Image file not found. Please check your path.")
        return

    model = load_model(model_path)

    img = load_img(image_path, target_size=(64, 64))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_labels[int(prediction[0][0] > 0.5)]
    confidence = float(prediction[0][0]) if predicted_class == 'dog' else (1 - float(prediction[0][0]))

    print(f"\n📸 Image: {os.path.basename(image_path)}")
    print(f"✅ Predicted: {predicted_class.upper()} (confidence: {confidence:.2f})")


# ==========================================================
# 🚀 MAIN EXECUTION LOGIC
# ==========================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🐾 Cat vs Dog Image Classifier")
    parser.add_argument("--train", action="store_true", help="Train the model")
    parser.add_argument("--predict", type=str, help="Path to image for prediction")
    parser.add_argument("--epochs", type=int, default=5, help="Number of training epochs")
    args = parser.parse_args()

    if args.train:
        train_model(epochs=args.epochs)
    elif args.predict:
        predict_image("models/cat_dog_model.h5", args.predict)
    else:
        print("⚠️ Please specify --train to train the model or --predict <image_path> to classify an image.")
