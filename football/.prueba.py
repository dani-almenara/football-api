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
                mensaje = json.loads(respuesta.text)
                return mensaje

print(obtener_datos_equipos())
