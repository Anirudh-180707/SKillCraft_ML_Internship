# House Price Prediction using Linear Regression

## SkillCraft Technology - Machine Learning Internship

### Task 1

---

## Project Overview

This project implements a Linear Regression model to predict house prices using selected property features from the House Prices dataset. The model learns the relationship between house characteristics and sale prices to estimate property values.

The project demonstrates the application of supervised machine learning techniques for regression problems and provides hands-on experience with data preprocessing, model training, prediction, and evaluation.

---

## Objective

To build a Linear Regression model that predicts house prices based on:

* Ground Living Area (Square Footage)
* Number of Bedrooms
* Number of Bathrooms

---

## Dataset

### Dataset Name

House Prices: Advanced Regression Techniques

### Source

Kaggle

### Dataset File Used

* train.csv

### Features Used

| Feature      | Description                             |
| ------------ | --------------------------------------- |
| GrLivArea    | Above-ground living area in square feet |
| BedroomAbvGr | Number of bedrooms above ground         |
| FullBath     | Number of full bathrooms                |
| SalePrice    | House sale price (Target Variable)      |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values by establishing a linear relationship between input features and the target variable.

In this project, the algorithm predicts house prices based on selected property characteristics.

---

## Project Workflow

### 1. Data Loading

The dataset is loaded using Pandas and inspected for relevant features.

### 2. Feature Selection

The following features are selected:

* GrLivArea
* BedroomAbvGr
* FullBath

Target Variable:

* SalePrice

### 3. Data Splitting

The dataset is divided into:

* Training Set (80%)
* Testing Set (20%)

### 4. Model Training

A Linear Regression model is trained using the training data.

### 5. Prediction

The trained model predicts house prices for unseen test data.

### 6. Model Evaluation

The model performance is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### 7. Visualization

A scatter plot is generated to compare actual house prices with predicted house prices.

---

## Results

### Model Performance

| Metric                         | Value     |
| ------------------------------ | --------- |
| Mean Absolute Error (MAE)      | 35,788.06 |
| Root Mean Squared Error (RMSE) | 52,975.72 |
| R² Score                       | 0.6341    |

The model achieved an R² score of approximately 63%, indicating that the selected features explain a significant portion of the variation in house prices.

---

## How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Directory

```bash
cd SCT_ML_1
```

### Install Required Libraries

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Run the Program

```bash
python house_price_prediction.py
```

---

## Output

The program displays:

* Model evaluation metrics
* Sample predicted house prices
* Actual vs Predicted House Price visualization

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Data Preprocessing
* Feature Selection
* Linear Regression
* Model Training
* Model Evaluation
* Regression Metrics
* Data Visualization
* Machine Learning Workflow

---

## Repository Structure

```text
SCT_ML_1
│
├── train.csv
├── house_price_prediction.py
└── README.md
```

---

## Author

Anirudh L

Machine Learning Intern

SkillCraft Technology
