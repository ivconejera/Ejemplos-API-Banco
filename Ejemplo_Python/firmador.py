# -*- coding: utf-8 -*-
import requests
# Importamos variales parametrizadas
from config import files, variables_generales, firmar
import jwt

rut_firmador = raw_input("Rut firmado:\n")

token = jwt.encode({'expiration': firmar.expiration, 'rut': rut_firmador, 'proposito': firmar.proposito, 'entidad': firmar.entidad},
                   variables_generales.SECRET,
                   algorithm='HS256')

####### Armamos Body
archivo1 = {}
archivo2 = {}
data = {}

data['token'] = token
data['api_token_key'] = variables_generales.APP_CODE
data['files'] = []

# Armamos json de archivo 1
archivo1['type'] = files.type_file1
archivo1['content'] = files.file1_base64
archivo1['checksum'] = files.checksum1_sha256
archivo1['description'] = files.description1
archivo1['layout'] = files.layout

# Armamos json de archivo 2
archivo2['type'] = files.type_file2
archivo2['content'] = files.file2_base64
archivo2['description'] = files.description2
archivo2['checksum'] = files.checksum2_sha256
#archivo2['layout'] = files.layout

# Archivo 1 y 2 en una lista []
data['files'].append(archivo1)
data['files'].append(archivo2)

# Subimos archivos y Obtenemos session
headers={"Content-Type": "application/json; charset=UTF-8", 'User-agent': 'Mozilla/5.0'}
r = requests.post(variables_generales.URL, json=data, headers=headers)
try:
    session_token = str(r.json()['session_token'])
except:
    print r.text
    exit()

otp = raw_input("OTP:\n")

# Firmamos Archivos subidos
headers={"Content-Type": "application/json; charset=UTF-8",
         "OTP": otp,
         'User-agent': 'Mozilla/5.0'}
r = requests.get(variables_generales.URL + "/" + session_token, headers=headers)
print r.text
