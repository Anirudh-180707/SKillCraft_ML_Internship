import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Dataset folder
DATASET_PATH = "train"

images = []
labels = []

cat_count = 0
dog_count = 0

print("Loading images...")

for filename in os.listdir(DATASET_PATH):

    filepath = os.path.join(DATASET_PATH, filename)

    if filename.startswith("cat"):

        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            img = cv2.resize(img, (64, 64))
            images.append(img.flatten())
            labels.append(0)
            cat_count += 1

    elif filename.startswith("dog"):

        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            img = cv2.resize(img, (64, 64))
            images.append(img.flatten())
            labels.append(1)
            dog_count += 1

print(f"\nCat Images: {cat_count}")
print(f"Dog Images: {dog_count}")
print(f"Total Images: {cat_count + dog_count}")

# Convert to NumPy Arrays
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