"""
Customer Segmentation using K-Means Clustering (Capstone Option 3)
Student Name: Vivek Vardhan | Machine Learning & AI
"""

import os
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def cluster_customers_pipeline():
    data_path = 'Mall_Customers.csv' if os.path.exists('Mall_Customers.csv') else os.path.join('data', 'Mall_Customers.csv')
    df_mall = pd.read_csv(data_path)
    print(f"Mall Customers dataset loaded. Shape: {df_mall.shape}")

    X_mall = df_mall[['Annual Income (k$)', 'Spending Score (1-100)']]

    # Fit K-Means with k=5 clusters
    km_mall = KMeans(n_clusters=5, init='k-means++', random_state=42)
    df_mall['Cluster'] = km_mall.fit_predict(X_mall)

    # Semantic Segment Labeling
    segment_labels = {
        0: 'Conservative Spenders (Low Spend, High Income)',
        1: 'Balanced Shoppers (Medium Income, Medium Spend)',
        2: 'High Value VIPs (High Income, High Spend)',
        3: 'Careful Youth (Low Income, Low Spend)',
        4: 'Impulsive Buyers (Low Income, High Spend)'
    }
    df_mall['Segment_Name'] = df_mall['Cluster'].map(segment_labels)
    print(df_mall[['CustomerID', 'Annual Income (k$)', 'Spending Score (1-100)', 'Segment_Name']].head())

    os.makedirs('models', exist_ok=True)
    joblib.dump(km_mall, os.path.join('models', 'mall_kmeans_model.joblib'))
    
    # Generate visualization
    plt.figure(figsize=(9, 6))
    colors = ['#E53E3E', '#3182CE', '#38A169', '#DD6B20', '#805AD5']
    for i, color in zip(range(5), colors):
        cluster_data = df_mall[df_mall['Cluster'] == i]
        plt.scatter(
            cluster_data['Annual Income (k$)'],
            cluster_data['Spending Score (1-100)'],
            s=60,
            c=color,
            label=segment_labels[i]
        )
    plt.scatter(
        km_mall.cluster_centers_[:, 0],
        km_mall.cluster_centers_[:, 1],
        s=180,
        c='black',
        marker='X',
        label='Centroids'
    )
    plt.title('Customer Segments (K-Means Clustering, k=5)', fontsize=14, fontweight='bold')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('static/customer_segments_clusters.png', dpi=300)
    plt.close()
    print("Saved clustering plot: static/customer_segments_clusters.png")

if __name__ == '__main__':
    cluster_customers_pipeline()
