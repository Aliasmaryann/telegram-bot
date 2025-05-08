import requests
from flask import Flask, request

app = Flask(__name__)

# Token de tu bot
TOKEN = '7832705502:AAFqWpFOZkoFROHMZS1ssT1KcHYhT8CnNX0'
URL = f"https://api.telegram.org/bot{TOKEN}/"

# Función para enviar mensajes
def send_message(chat_id, text):
    url = URL + f"sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

# Ruta que maneja los updates (mensajes recibidos)
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # Lógica para responder a los mensajes
    if text.lower() == '/start':
        send_message(chat_id, "¡Bienvenido al bot!")
    elif text.lower() == 'info':
        send_message(chat_id, "Este es un bot de ejemplo.")
    else:
        send_message(chat_id, "No entiendo ese comando.")

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
