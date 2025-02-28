# importazione delle libreie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Caricamento del dataset
data = load_iris()
X = data.data # caratteristiche
y = data.target # etichette

# divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# creazione del modello di classificazione
model = RandomForestClassifier(n_estimators=100, random_state=42)

#addestramento del modello
model.fit(X_train, y_train)

#predizione delle etichette per il set di test
predictions = model.predict(X_test)

# calcolo dell'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")