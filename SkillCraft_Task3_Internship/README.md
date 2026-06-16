# Cats vs Dogs Classification using Support Vector Machine (SVM)

## SkillCraft Technology - Machine Learning Internship

### Task 3

---

## Project Overview

This project implements a Support Vector Machine (SVM) classifier to distinguish between images of cats and dogs. The model is trained using image data from the Dogs vs Cats dataset and learns visual patterns that help classify unseen images accurately.

The project demonstrates the application of machine learning techniques in image classification and computer vision.

---

## Objective

To build an SVM-based image classification model capable of identifying whether an image belongs to a cat or a dog.

---

## Dataset

### Dataset Name

Dogs vs Cats Dataset

### Source

Kaggle

### Dataset Link

https://www.kaggle.com/c/dogs-vs-cats/data

### Dataset Files Used

* train.zip (Extracted)

### Classes

* Cat
* Dog

### Total Images Used

1049 Images

---

## Technologies Used

* Python
* NumPy
* OpenCV (cv2)
* Scikit-learn

---

## Machine Learning Algorithm

### Support Vector Machine (SVM)

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification tasks. It finds an optimal decision boundary that separates different classes with maximum margin.

In this project, SVM is used to classify images into:

* Cat
* Dog

---

## Project Workflow

### 1. Data Collection

The Dogs vs Cats dataset was downloaded from Kaggle.

### 2. Image Preprocessing

* Convert images to grayscale
* Resize images to 64 × 64 pixels
* Flatten image pixels into feature vectors

### 3. Label Assignment

* Cat → 0
* Dog → 1

### 4. Data Splitting

The dataset is divided into training and testing sets.

### 5. Model Training

An SVM classifier with a linear kernel is trained using the processed image data.

### 6. Prediction

The trained model predicts labels for unseen images.

### 7. Evaluation

Model performance is measured using:

* Accuracy Score
* Classification Report

---

## Output

The program displays:

* Number of Cat Images Loaded
* Number of Dog Images Loaded
* Total Images Loaded
* Model Accuracy
* Classification Report

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Image Processing
* Feature Extraction
* Computer Vision Fundamentals
* Supervised Learning
* Support Vector Machines
* Image Classification
* Model Evaluation

---

## Repository Structure

```text
SCT_ML_3/
│
├── train/
│   ├── cat.0.jpg
│   ├── cat.1.jpg
│   ├── ...
│   ├── dog.0.jpg
│   ├── dog.1.jpg
│   └── ...
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
