# утилиты

import json
import sys

sys.path.append('../')
from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from decos import log

@log
def get_message(client):
    # Утилита приема и декодирования сообщения. Прием байтов, выдача словаря.

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError



@log
def send_message(sock, message):

    # утилита кодирования и отправки сообщения. принимает словарь, получает из него стоку. переводит в байты и отправляет

    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)