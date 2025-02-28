from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Caricamento del dataset
diabetes= load_diabetes()
X= diabetes.data
y=diabetes.target
df = pd.DataFrame(X, columns=diabetes.feature_names)
df['target'] = y

#esplora
print(df.head())
print(df.info())
print(df.describe())
print(df['target'].value_counts())

# Suddivisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo dell'errore quadratico medio
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


# Calcolo dell'r2
r2 = r2_score(y_test, y_pred)
print("r2:", r2)

# Selezioniamo la prima caratteristica di X_test
X_test_feature = X_test[:, 0]  # Prima caratteristica di X_test
y_pred_feature = y_pred  # Predizioni del modello

# Calcolare la linea di regressione: y = m * X + b
m_pred, b_pred = np.polyfit(X_test_feature, y_pred_feature, 1)  # Calcola m e b per i valori predetti
line_pred = m_pred * X_test_feature + b_pred  # Linea di regressione

# Crea uno scatter plot con la linea di regressione
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, label='Valori Predetti')
sns.regplot(x=y_test, y=y_pred, scatter=False, color='red', label='Linea di Regressione')
plt.xlabel('Valori Reali')
plt.ylabel('Valori Predetti')
plt.title('Scatter Plot dei Valori Reali vs Valori Predetti con Linea di Regressione')
plt.legend()
plt.show()