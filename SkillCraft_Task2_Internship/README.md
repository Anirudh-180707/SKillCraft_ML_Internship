# Customer Segmentation using K-Means Clustering

## SkillCraft Technology - Machine Learning Internship

### Task 2

---

## Project Overview

This project implements the K-Means Clustering algorithm to segment customers of a retail store based on their annual income and spending behavior.

Customer segmentation helps businesses understand different customer groups and develop targeted marketing strategies, improve customer engagement, and optimize product offerings.

---

## Objective

To group customers into distinct clusters using the K-Means clustering algorithm based on:

* Annual Income
* Spending Score

---

## Dataset

### Dataset Name

Mall Customer Dataset

### Dataset File Used

* Mall_Customers.csv

### Features Available

| Feature                | Description                       |
| ---------------------- | --------------------------------- |
| CustomerID             | Unique customer identifier        |
| Gender                 | Customer gender                   |
| Age                    | Customer age                      |
| Annual Income (k$)     | Annual income in thousand dollars |
| Spending Score (1-100) | Customer spending behavior score  |

### Features Used for Clustering

| Feature                |
| ---------------------- |
| Annual Income (k$)     |
| Spending Score (1-100) |

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised machine learning algorithm used to divide data into clusters based on similarity.

The algorithm:

1. Selects a predefined number of clusters (K).
2. Assigns data points to the nearest cluster centroid.
3. Updates centroids iteratively.
4. Repeats until convergence.

---

## Project Workflow

### 1. Data Loading

The Mall Customer dataset is loaded using Pandas.

### 2. Feature Selection

The following features are selected:

* Annual Income (k$)
* Spending Score (1-100)

### 3. Elbow Method

The Elbow Method is used to determine the optimal number of clusters by analyzing the Within-Cluster Sum of Squares (WCSS).

### 4. Model Training

K-Means Clustering is applied with 5 clusters.

### 5. Visualization

Customer segments and cluster centroids are visualized using scatter plots.

---

## Results

### Optimal Number of Clusters

Using the Elbow Method, the optimal number of customer segments was identified as:

```text
5 Clusters
```

### Customer Segments

The model successfully grouped customers into distinct clusters based on their spending behavior and annual income.

Possible segments include:

* High Income, High Spending
* High Income, Low Spending
* Low Income, High Spending
* Low Income, Low Spending
* Average Customers

---

## How to Run

### Install Required Libraries

```bash
pip install pandas matplotlib scikit-learn
```

### Run the Program

```bash
python main.py
```

---

## Output

The program generates:

* Dataset Preview
* Elbow Method Graph
* Customer Segmentation Visualization
* Cluster Distribution Summary

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Unsupervised Learning
* K-Means Clustering
* Customer Segmentation
* Data Visualization
* Elbow Method
* Cluster Analysis
* Exploratory Data Analysis

---

## Repository Structure

```text
SCT_ML_2/
│
├── Mall_Customers.csv
├── main.py
└── README.md
```

---

## Author

Anirudh L

Machine Learning Intern

SkillCraft Technology
