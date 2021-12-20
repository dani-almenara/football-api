#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from datetime import datetime
from datetime import timedelta
import time
from decouple import config
def obtener_datos_equipos():
        url = "http://api.football-data.org/v3/competitions/PD/teams"
        headers = {"X-Auth-Token":config("TOKEN_FOOTBALL"),}
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
                mensaje = json.loads(respuesta.content)
                return mensaje


respuesta = obtener_datos_equipos()

# ahora hay que evaluar la respuesta
# con el json.load, has pasado de json a diccionario de python
#aqui veras el resultado
print(respuesta)

# para ver una clave concreta
print(list(respuesta))

