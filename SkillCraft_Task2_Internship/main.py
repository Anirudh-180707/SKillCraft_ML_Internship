import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Dataset
df = pd.read_csv("Mall_Customers.csv")

# Display First 5 Rows
print("\nDataset Preview:")
print(df.head())

# Select Features for Clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# -------------------------------
# Elbow Method to Find Optimal K
# -------------------------------
wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# -------------------------------
# Apply K-Means Clustering
# -------------------------------
kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X)

# Add Cluster Labels to Dataset
df['Cluster'] = clusters

# -------------------------------
# Visualize Customer Segments
# -------------------------------
plt.figure(figsize=(10, 6))

plt.scatter(
    X.iloc[clusters == 0, 0],
    X.iloc[clusters == 0, 1],
    label='Cluster 1'
)

plt.scatter(
    X.iloc[clusters == 1, 0],
    X.iloc[clusters == 1, 1],
    label='Cluster 2'
)

plt.scatter(
    X.iloc[clusters == 2, 0],
    X.iloc[clusters == 2, 1],
    label='Cluster 3'
)

plt.scatter(
    X.iloc[clusters == 3, 0],
    X.iloc[clusters == 3, 1],
    label='Cluster 4'
)

plt.scatter(
    X.iloc[clusters == 4, 0],
    X.iloc[clusters == 4, 1],
    label='Cluster 5'
)

# Cluster Centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300,
    marker='X',
    label='Centroids'
)

plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# Cluster Summary
# -------------------------------
print("\nCustomer Segmentation Completed Successfully!")

print("\nNumber of Customers in Each Cluster:")
print(df['Cluster'].value_counts().sort_index())