from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score, homogeneity_score, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA

iris= load_iris()
X= iris.data
y=iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

#esplora
print(df.head())
print(df.info())
print(df.describe())
print(df['target'].value_counts())


# Creazione del modello K-Means
kmeans = KMeans(
        n_clusters=3,
        init='k-means++',
        n_init=10,
        max_iter=300,
        tol=1e-4,
        random_state=42)

# Addestramento del modello
kmeans.fit(X)

# Predizione dei cluster
y_pred = kmeans.predict(X)



# Calcolo degli score
print("Rand Adjusted:")
a_d_s = adjusted_rand_score(y, y_pred)  # Passa i target veri e i target predetti
print(a_d_s)

print("Homogeneity Score:")
h_s = homogeneity_score(y, y_pred)  # Passa i target veri e i target predetti
print(h_s)



plt.figure(figsize=(12, 6))
#Subplot 1 (stesso grafico di prima per i cluster)
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis')
centri = kmeans.cluster_centers_
plt.scatter(centri[:, 0], centri[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clustering con K-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
#Subplot 2
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis')
plt.title('Etichette Reali delle Specie di Iris')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

# Applica PCA per ridurre a 2 dimensioni
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)  # Proietta i dati sulle prime 2 componenti principali

# Scatter plot delle prime due componenti principali
# 


plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=50)
plt.xlabel('PCA Feature 1')
plt.ylabel('PCA Feature 2')
plt.title('Iris Dataset - Prime Due Componenti Principali')
plt.colorbar(label="Classi Iris")
plt.show()