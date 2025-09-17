"""
🤖 Chatbot Básico con Reglas
--------------------------------
Un chatbot simple que responde a preguntas comunes usando
coincidencia de palabras clave.
"""

def responder(pregunta):
    pregunta = pregunta.lower()
    if "hola" in pregunta:
        return "👋 ¡Hola! ¿En qué puedo ayudarte?"
    elif "adios" in pregunta or "gracias" in pregunta:
        return "😊 ¡Hasta luego!"
    elif "nombre" in pregunta:
        return "🤖 Soy un chatbot básico en Python."
    else:
        return "❓ No entendí tu pregunta. Intenta con otra."

if __name__ == "__main__":
    print("🤖 Chatbot iniciado. Escribe 'salir' para terminar.\n")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("👋 Adiós!")
            break
        respuesta = responder(user_input)
        print(f"Bot: {respuesta}")
