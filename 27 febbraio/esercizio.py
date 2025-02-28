from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,  confusion_matrix
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV

# carica il dataset Iris
data = load_wine()
X = data.data 
y = data.target

# Creare un DataFrame 
df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y  # Aggiungere la colonna target

# Mostrare le prime righe
#print(df.head())

#numero campioni
print(df['target'].value_counts())


# statistiche
#print(df.describe())

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# suddividi i dati in trainig e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =42)

modello = RandomForestClassifier()
modello.fit(X_train,y_train)
y_predict = modello.predict(X_test)

accuracy = accuracy_score(y_predict, y_test)

# 6. Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_predict)

# Visualizzazione della matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
xticklabels=data.target_names,
yticklabels=data.target_names)
plt.xlabel('Predicted') 
plt.ylabel('Actual') 
plt.title('Confusion Matrix') 
plt.show()



# Parametri per GridSearch
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20]
}

grid_search = GridSearchCV(modello, param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(f"Migliori parametri: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_}")