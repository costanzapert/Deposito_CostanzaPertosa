from sklearn.datasets import  load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# carica
data = load_iris()
X = data.data
y=data.target 

#scala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# suddiviosine
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size= 0.3, random_state = 42)

# modello
modello = DecisionTreeClassifier(random_state=42)
modello.fit(X_train,y_train)
y_pred = modello.predict(X_test)

#valuta
accuracy = classification_report(y_pred, y_test, target_names=data.target_names)
print(accuracy)

# matrice di confusione
A = confusion_matrix(y_test, y_pred)
print(A)

