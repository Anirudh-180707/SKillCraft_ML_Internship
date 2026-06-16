# Hand Gesture Recognition using Support Vector Machine (SVM)

## SkillCraft Technology - Machine Learning Internship

### Task 4

---

## Project Overview

This project implements a Hand Gesture Recognition system using a Support Vector Machine (SVM) classifier. The model is trained on the LeapGestRecog dataset and is capable of recognizing multiple hand gestures from image data.

The project demonstrates the application of machine learning and computer vision techniques for gesture-based classification and human-computer interaction.

---

## Objective

To develop a machine learning model capable of accurately recognizing and classifying different hand gestures from image data.

---

## Dataset

### Dataset Name

LeapGestRecog Dataset

### Source

Kaggle

### Dataset Link

https://www.kaggle.com/datasets/gti-upm/leapgestrecog

### Classes

* Palm
* L
* Fist
* Fist Moved
* Thumb
* Index
* OK
* Palm Moved
* C
* Down

### Images Used

10,000 Images

### Dataset Note

The original dataset is too large to upload directly to GitHub. Therefore, the dataset is not included in this repository.

To run this project:

1. Download the dataset from Kaggle.
2. Extract the dataset.
3. Place the extracted folder in the project directory.

---

## Technologies Used

* Python
* NumPy
* OpenCV (cv2)
* Scikit-learn

---

## Machine Learning Algorithm

### Support Vector Machine (SVM)

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification tasks. It identifies optimal decision boundaries between classes and performs effectively for image classification problems.

---

## Project Workflow

### 1. Data Loading

Gesture images are loaded from the LeapGestRecog dataset.

### 2. Image Preprocessing

* Convert images to grayscale
* Resize images to 64 × 64 pixels
* Flatten image data into feature vectors

### 3. Data Preparation

* Assign gesture labels
* Convert images into numerical feature vectors

### 4. Train-Test Split

The dataset is divided into training and testing sets.

### 5. Model Training

An SVM classifier with a linear kernel is trained using the processed image data.

### 6. Prediction

The trained model predicts gesture classes for unseen images.

### 7. Evaluation

Model performance is evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score

---

## Results

### Model Accuracy

99.85%

The model achieved excellent classification performance across all gesture classes.

---

## Warning Messages Observed During Execution

While running the program, OpenCV generated warnings similar to:

```text
imread_('archive\\leapGestRecog\\00\\01_palm'):
can't open/read file
```

These warnings occurred because the dataset contains gesture folders before the actual image files. The program briefly attempted to read folder names as image files.

These warnings did not affect model training or prediction, as the actual image files were loaded correctly afterward.

Final Output:

* Total Images Loaded: 10,000
* Model Accuracy: 99.85%

---

## Learning Outcomes

* Computer Vision Fundamentals
* Image Processing
* Feature Extraction
* Gesture Recognition
* Supervised Learning
* Support Vector Machines
* Model Evaluation

---

## Repository Structure

```text
SCT_ML_4/
│
├── archive/
│   └── leapGestRecog/
│
├── main.py
└── README.md
```

---

## Installation

```bash
pip install opencv-python numpy scikit-learn
```

---

## Run the Project

```bash
python main.py
```

---

## Author

Anirudh L

Machine Learning Intern

SkillCraft Technology
