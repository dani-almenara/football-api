#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Devuelve todos los equipos de la liga española

import requests
import json
from datetime import datetime
from datetime import timedelta
import time
from decouple import config
def obtener_datos():
	url = "http://api.football-data.org/v2/competitions/PD/teams"
	headers = {"Content-type": "*/*", "X-Auth-Token":"0dc688c1cdb64e5aa8df5d5ebceb5148"}
	respuesta = requests.get(url, headers=headers)
	if respuesta.status_code == 200:
		mensaje = json.loads(respuesta.text)
		return mensaje

print(obtener_datos())
