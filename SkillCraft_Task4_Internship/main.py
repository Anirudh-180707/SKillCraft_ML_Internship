import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Dataset folder
DATASET_PATH = "archive"

images = []
labels = []

print("Loading gesture images...")

for user_folder in os.listdir(DATASET_PATH):

    user_path = os.path.join(DATASET_PATH, user_folder)

    if not os.path.isdir(user_path):
        continue

    for gesture_folder in os.listdir(user_path):

        gesture_path = os.path.join(user_path, gesture_folder)

        if not os.path.isdir(gesture_path):
            continue

        label = gesture_folder

        image_count = 0

        for image_file in os.listdir(gesture_path):

            image_path = os.path.join(gesture_path, image_file)

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            # Resize image
            img = cv2.resize(img, (64, 64))

            # Convert image to feature vector
            images.append(img.flatten())

            # Store label
            labels.append(label)

            image_count += 1

            # Limit images per gesture for faster training
            if image_count >= 100:
                break

print(f"\nTotal Images Loaded: {len(images)}")

# Convert to NumPy arrays
X = np.array(images)
y = np.array(labels)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining SVM Model...")

# Train SVM
model = SVC(kernel="linear")

model.fit(X_train, y_train)

print("Making Predictions...")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))