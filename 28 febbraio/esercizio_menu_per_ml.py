#Creare un menu di selezione, 1 generazione, 2 analisi descrittiva, 
# 3 grafico riguardate i dati, 4 attivare i risultati del classification report ML
import pandas as pd
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


while True:
    print("Menu")
    print("Seleziona 1 per caricare il dataset")
    print("Seleziona 2 per effettuare un'analisi descrittiva")
    print("Seleziona 3 per effettuare un grafico riguardate i dati")
    print("Seleziona 4 attivare i risultati del classification report ML")
    print("Seleziona 5 per uscire")
    scelta = input("")
    if scelta == "1":
        wine= load_wine()
        X= wine.data
        y=wine.target
        df = pd.DataFrame(X, columns=wine.feature_names)
        df['target'] = y
        print("Dataset caricato")
    elif scelta == "2":
        print(df.describe())
    elif scelta == "3":
        # Contare le occorrenze di ciascun target
        target_counts = df['target'].value_counts().sort_index()

        # Creare il grafico a barre
        plt.figure(figsize=(8, 5))
        plt.bar(target_counts.index, target_counts.values, color=['blue', 'orange', 'green'])
        plt.xlabel('Classi del vino')
        plt.ylabel('Frequenza')
        plt.title('Distribuzione delle classi nel dataset Wine')
        plt.xticks(target_counts.index, [f'Classe {i}' for i in target_counts.index])
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Mostrare il grafico
        plt.show()
        
    elif scelta == "4":
        # Suddivisione dei dati in training e test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Creazione del modello di classificazione
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Addestramento del modello
        model.fit(X_train, y_train)

        # Predizione sui dati di test
        y_pred = model.predict(X_test)
    
        # 5. Valuta la performance del modello utilizzando il classification_report
        report = classification_report(y_test, y_pred, target_names=wine.target_names)
        print("Classification Report:\n", report)

    elif scelta ==  "5":
        break
    