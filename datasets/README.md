# 🤖 Portafolio Nivel 4 – Machine Learning y Proyectos Aplicados

Este repositorio contiene proyectos de **Nivel Avanzado** enfocados en **Machine Learning**, **procesamiento de datos** y **automatización inteligente**.  
El objetivo de este nivel es demostrar mi capacidad para **entrenar modelos**, **clasificar datos** y **crear soluciones prácticas** que usen inteligencia artificial.

---

## 🧾 Tabla de Contenidos
1. [🖼️ Clasificador de Imágenes (CNN)](#-1-clasificador-de-imágenes-cnn)
2. [💬 Chatbot Básico (NLP)](#-2-chatbot-básico-nlp)
3. [📊 Predicción de Ventas (Regresión)](#-3-predicción-de-ventas-regresión)
4. [🚀 Instalación y Uso](#-instalación-y-uso)
5. [🛠 Tecnologías Usadas](#-tecnologías-usadas)
6. [🎯 Habilidades Desarrolladas](#-habilidades-desarrolladas)
7. [📌 Próximos Pasos](#-próximos-pasos)

---

### 🖼️ 1. Clasificador de Imágenes (CNN)

Un modelo de **red neuronal convolucional (CNN)** entrenado en un dataset pequeño para clasificar imágenes.  
Por defecto usa el dataset **MNIST Fashion** (camisetas, zapatos, bolsos, etc.), pero es fácil reemplazarlo por imágenes de frutas, animales o tus propios datos.

✅ **Características:**
- Entrenamiento en **Keras + TensorFlow**
- Métricas de precisión, matriz de confusión y gráfica de pérdida/accuracy
- Predicción en nuevas imágenes (subiendo archivos)

📸 *Ejemplo de ejecución:*  
![Clasificador de Imágenes](assets/clasificador.png)

#### 🔑 Recomendaciones para reproducirlo
- Usar entornos virtuales (`python -m venv venv`) para aislar dependencias.
- Si tu PC es modesta, entrena en menos épocas (`epochs=5`) para reducir tiempo.
- Para probar con tus imágenes, guárdalas en una carpeta `imagenes_prueba/` y actualiza el script para preprocesarlas.

---

### 💬 2. Chatbot Básico (NLP)

Un pequeño **chatbot basado en reglas y machine learning**, usando **NLTK + scikit-learn**, que responde preguntas predefinidas.

✅ **Características:**
- Procesa texto de usuario, elimina stopwords y vectoriza
- Usa clasificación simple para elegir la respuesta
- Ideal como demo de procesamiento de lenguaje natural

📸 *Ejemplo de conversación:*  
![Chatbot](assets/chatbot.png)

---

### 📊 3. Predicción de Ventas (Regresión)

Un modelo de **regresión lineal** que predice ventas futuras en base a datos históricos.  
Incluye un pequeño dashboard con Matplotlib para visualizar las tendencias.

📸 *Captura de ejemplo:*  
![Predicción de Ventas](assets/regresion.png)

---

## 🚀 Instalación y Uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/iparra-sys/Portafolio-Nivel-4.git
cd Portafolio-Nivel-4

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar proyectos
python clasificador_imagenes.py
python chatbot.py
python prediccion_ventas.py

```

--- 

## 🛠 Tecnologías Usadas

Python 3.13
TensorFlow / Keras (para redes neuronales)
scikit-learn (para ML clásico)
NLTK (para NLP)
Matplotlib y Seaborn (para visualización)
pandas y numpy (para manipulación de datos)

## 🎯 Habilidades Desarrolladas

Machine Learning supervisado: clasificación y regresión
Procesamiento de imágenes: uso de CNNs y normalización
Procesamiento de texto: tokenización, stopwords, bag of words
Visualización de métricas: accuracy, pérdida, matriz de confusión
Automatización de pruebas: predicciones en datos nuevos

## 📌 Próximos Pasos

🚀 En las siguientes iteraciones incluiré:
✅ Modelos más complejos con transfer learning (ej. MobileNet, ResNet)
✅ Chatbot con integración a OpenAI API para respuestas dinámicas
✅ Despliegue de modelos en Streamlit para usarlos en la web
