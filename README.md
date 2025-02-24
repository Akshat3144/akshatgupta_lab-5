# MLPR LAB 5 - Distance Classification

## Overview
This project implements distance-based classification using K-Means clustering on face detection features (hue and saturation) extracted from facial images (`Plaksha_Faculty.jpg` and `Dr_Shashi_Tharoor.jpg`). It adheres to best practices for version control, automation, containerization, and experiment tracking, as outlined in the assignment requirements. The project includes three key Jupyter Notebook files:

- `akshatgupta_lab-5.ipynb`: The completed notebook with all code implementations for face detection, feature extraction, K-Means clustering, and visualizations.
- `kaggle_notebook.ipynb`: The notebook downloaded from Kaggle after integrating Weights & Biases (Wandb) for experiment tracking, including logged metrics (e.g., Silhouette Score, Inertia) and visualizations (e.g., clustering plots, histograms).
- `distance_classification.ipynb`: The notebook optimized for GitHub Actions automation, built on top of `kaggle_notebook.ipynb`, and configured to run seamlessly while logging results to Wandb.

-------------------------------------

## Output Plots:
![1740391376567](image/README/1740391376567.png)
![1740391393867](image/README/1740391393867.png)
![1740391402235](image/README/1740391402235.png)
![1740391410953](image/README/1740391410953.png)

-------------------------------------

## Report:
## Answer the following questions within your report:

#### 1. What are the common distance metrics used in distance-based classification algorithms? 
Common distance metrics used in distance-based classification algorithms include Euclidean distance, Manhattan distance, Mahalanobis distance, Minkowski distance, and Cosine similarity. These metrics determine how similar or different two data points are based on their feature values.

#### 2. What are some real-world applications of distance-based classification algorithms?
Real-world applications of distance-based classification algorithms include recommender systems, image recognition, anomaly detection, medical diagnosis, and text classification. For example, KNN is used in disease prediction by comparing a patient’s symptoms with past cases.

#### 3. Explain various distance metrics. 
- Euclidean Distance: Measures straight-line distance between two points in space.
- Manhattan Distance: Computes distance by summing absolute differences along each dimension.
- Mahalanobis Distance: Accounts for correlations between variables, making it useful for detecting outliers in multivariate data.
- Minkowski Distance: A generalized form of Euclidean and Manhattan distance.
- Cosine Similarity: Measures the angle between two vectors, often used in text analysis.

#### 4. What is the role of cross validation in model performance? 
Cross-validation helps assess model performance by splitting data into multiple training and testing sets. It prevents overfitting and ensures the model generalizes well to unseen data by providing an unbiased evaluation of its predictive ability.

#### 5. Explain variance and bias in terms of KNN? 
In KNN, high bias occurs when K is large, leading to oversimplification and underfitting. High variance occurs when K is small, making the model sensitive to noise and prone to overfitting. A balanced K value helps optimize the bias-variance tradeoff.

-------------------------------------
## Wandb Project Dashboard:
![1740391538618](image/README/1740391538618.png)
![1740391600298](image/README/1740391600298.png)
![1740415926249](image/README/1740415926249.png)
![1740391636830](image/README/1740391636830.png)
![1740391651811](image/README/1740391651811.png)
![1740391680246](image/README/1740391680246.png)
![1740395310384](image/README/1740395310384.png)
![1740415973847](image/README/1740415973847.png)
