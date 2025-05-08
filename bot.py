import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Obtener el token desde las variables de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].lower()  
        response = handle_message(text)
        send_message(chat_id, response)
    return "OK"

def handle_message(text):
    """
    Función que maneja los mensajes entrantes y devuelve una respuesta.
    """
    if text == "/start":
        return "¡Bienvenido al bot de Maria Arias!"
    elif text == "hola":
        return "¡Hola! ¿Cómo estás?"
    elif text == "info":
        return "Soy el bot de Maria Arias, creado para ayudarte."
    elif text == "como estas":
        return "Estoy bien, gracias por preguntar."
    else:
        return "No te he entendido. Intenta con /start, hola, info o '¿cómo estás?'"

def send_message(chat_id, text):
    """
    Función para enviar un mensaje al usuario de Telegram.
    """
    message_url = f"{URL}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(message_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
