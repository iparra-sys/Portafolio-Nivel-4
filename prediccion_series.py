"""
📊 Predicción de Series Temporales
--------------------------------
Este script usa scikit-learn para predecir valores futuros de
una serie de datos (ej. ventas mensuales).
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

CSV_FILE = "datasets/ventas.csv"

def cargar_datos():
    if not os.path.exists(CSV_FILE):
        print("⚠️ No se encontró el archivo 'ventas.csv'.")
        return None
    df = pd.read_csv(CSV_FILE)
    if "Mes" not in df.columns or "Ventas" not in df.columns:
        print("⚠️ El CSV debe contener las columnas 'Mes' y 'Ventas'.")
        return None
    return df

if __name__ == "__main__":
    df = cargar_datos()
    if df is not None:
        X = np.arange(len(df)).reshape(-1, 1)
        y = df["Ventas"].values
        modelo = LinearRegression()
        modelo.fit(X, y)

        # Predicción de próximos 3 meses
        futuros = np.arange(len(df), len(df) + 3).reshape(-1, 1)
        predicciones = modelo.predict(futuros)

        plt.figure(figsize=(8, 4))
        plt.plot(df["Mes"], y, label="Histórico", marker="o")
        plt.plot([f"Futuro {i+1}" for i in range(3)], predicciones, label="Predicción", marker="x")
        plt.legend()
        plt.title("📈 Predicción de Series Temporales")
        plt.xlabel("Mes")
        plt.ylabel("Ventas")
        plt.show()
