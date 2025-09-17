"""
📊 Predicción de Series Temporales
--------------------------------
Script que entrena un modelo de regresión lineal para predecir
los próximos valores de una serie de datos (ej. ventas mensuales).
Genera un dataset de ejemplo si no encuentra el CSV.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

CSV_FILE = "datasets/ventas.csv"

def generar_dataset_ejemplo():
    """Crea un CSV con datos ficticios si no existe."""
    print("📁 No se encontró 'ventas.csv', generando dataset de ejemplo...")
    os.makedirs("datasets", exist_ok=True)
    datos = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Ventas": [120, 150, 180, 170, 200, 210],
        "Categoria": ["A", "A", "B", "B", "C", "C"]  # Columna extra opcional
    }
    df = pd.DataFrame(datos)
    df.to_csv(CSV_FILE, index=False)
    return df

def cargar_datos():
    """Carga datos del CSV o genera uno de ejemplo."""
    if not os.path.exists(CSV_FILE):
        return generar_dataset_ejemplo()
    df = pd.read_csv(CSV_FILE)

    # Validación flexible: solo necesitamos Mes y Ventas
    columnas = df.columns
    if "Mes" not in columnas or "Ventas" not in columnas:
        print("⚠️ El CSV debe contener al menos las columnas 'Mes' y 'Ventas'.")
        return None

    # Filtramos solo columnas relevantes
    df = df[["Mes", "Ventas"]]
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

        # Mostrar predicciones en consola
        print("\n🔮 Predicciones de los próximos meses:")
        for i, p in enumerate(predicciones, 1):
            print(f"Mes Futuro {i}: {p:.2f} unidades")

        # Graficar
        plt.figure(figsize=(8, 4))
        plt.plot(df["Mes"], y, label="Histórico", marker="o")
        plt.plot([f"Futuro {i}" for i in range(1, 4)], predicciones,
                 label="Predicción", marker="x", linestyle="--")
        plt.legend()
        plt.title("📈 Predicción de Series Temporales")
        plt.xlabel("Mes")
        plt.ylabel("Ventas")
        plt.grid(alpha=0.3)
        plt.tight_layout()

        # Guardar y mostrar
        plt.savefig("prediccion_series.png")
        print("\n✅ Gráfica guardada como 'prediccion_series.png'")
        plt.show()
