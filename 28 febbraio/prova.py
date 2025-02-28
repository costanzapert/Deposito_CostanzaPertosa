


# Stampa dei coefficienti
print("Coefficienti:", model.coef_)
print("Intercetta:", model.intercept_)


# Grafico con i valori predetti e la linea di regressione
plt.scatter(X_test_feature, y_pred_feature, color='blue', label="Predizioni")
plt.plot(X_test_feature, line_pred, color='red', label="Linea di regressione (Predizioni)")
plt.xlabel("Caratteristica 1 (X_test[:, 0])")
plt.ylabel("Valori Predetti (y_pred)")
plt.title("X_test vs y_pred con Linea di Regressione")
plt.legend()
plt.show()


# Calcolare la linea di regressione per i valori reali
m_real, b_real = np.polyfit(X_test_feature, y_test, 1)  # Calcola m e b per i valori reali
line_real = m_real * X_test_feature + b_real  # Linea di regressione per i valori reali

# Grafico con i valori reali e la linea di regressione
plt.scatter(X_test_feature, y_test, color='green', label="Valori Reali")
plt.plot(X_test_feature, line_real, color='orange', label="Linea di regressione (Reali)")
plt.xlabel("Caratteristica 1 (X_test[:, 0])")
plt.ylabel("Valori Reali (y_test)")
plt.title("X_test vs y_test con Linea di Regressione")
plt.legend()
plt.show()
