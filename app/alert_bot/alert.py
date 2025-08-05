import requests
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN_TELEGRAM')
CHAT_ID = os.getenv('CHAT_ID')


def enviar_mensaje(mensaje):
    tex = mensaje
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {
        'chat_id': CHAT_ID,
        'text': tex
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Mensaje enviado correctamente")
    else:
        print("Error al enviar mensaje:", response.text)


