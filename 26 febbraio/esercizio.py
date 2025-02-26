from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# carica il dataset Iris
data = load_iris()
X = data.data 
y = data.target

# suddividi i dati in trainig e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state =42)

# applica l'algoritmo K_Nearest Neighbors con n_n = 5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)

# valuta la performance del moello usando l'accuratezza
accuracy = accuracy_score(predictions, y_test)

print(accuracy)

# sia per test_size = 0.3 che 0.2 l'accurancy è 1
# ho cambiato random_state = 3 ed ho accuratezza 0.95 periodico con test_size = 0.3
# random_state = 1 test_size = 0.3 ho accuratezza 0.9777777777777777

