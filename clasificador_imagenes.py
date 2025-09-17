"""
📂 Clasificador de Imágenes Optimizado
--------------------------------
Entrena un modelo de clasificación de imágenes usando TensorFlow/Keras
con validación, aumentación de datos y guardado en formato moderno .keras
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import os

# --- CONFIGURACIÓN ---
DATASET_DIR = "datasets/frutas"  # Ajusta la ruta a tu dataset
IMG_SIZE = (64, 64)
BATCH_SIZE = 16
VALIDATION_SPLIT = 0.2
SEED = 123
EPOCHS = 10  # Ajusta según el tamaño de tu dataset

# --- FUNCIONES ---
def cargar_dataset():
    if not os.path.exists(DATASET_DIR):
        print("⚠️ No se encontró el dataset. Asegúrate de tener 'datasets/frutas'")
        return None, None, None

    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR,
        validation_split=VALIDATION_SPLIT,
        subset="training",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR,
        validation_split=VALIDATION_SPLIT,
        subset="validation",
        seed=SEED,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    class_names = train_ds.class_names  # Guardar antes del prefetch

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, class_names

def construir_modelo(num_clases):
    model = models.Sequential([
        layers.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
        layers.Rescaling(1./255),

        # --- Aumentación de datos ---
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),

        layers.Conv2D(32, (3, 3), activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(num_clases, activation="softmax")
    ])

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model

# --- SCRIPT PRINCIPAL ---
if __name__ == "__main__":
    train_ds, val_ds, class_names = cargar_dataset()
    if train_ds and val_ds:
        print(f"✅ Dataset cargado con {len(class_names)} clases: {class_names}")
        print(f"📊 Número de batches de entrenamiento: {len(train_ds)}, validación: {len(val_ds)}")

        model = construir_modelo(len(class_names))
        print(f"🚀 Entrenando modelo durante {EPOCHS} epochs...")
        model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)

        model.save("modelo_clasificador.keras")
        print("💾 Modelo guardado en formato moderno como 'modelo_clasificador.keras'")
