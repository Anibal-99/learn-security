"""
El endpoint para resolver este ejercicio no existe en esta seccion
del WebGoat, por ende lo que hice fue analizar el codigo fuente en su repositorio
https://github.com/WebGoat/WebGoat

lo que hice fue analizar donde estaba el codigo de las secciones de los
ejercicios 2 y 3. Tambien me fije en el archivo SQL como eran las credenciales
del usuario Jerry

"""

import hashlib # libreria para generar hash seguros, como el sha265
import base64 # para codificar y decodificar en base64

# variables necesarias que saque del codigo fuente
password = "doesnotreallymatter"
username = "Jerry"
passwordSaltWeak = "DeliberatelyInsecure1234"
passwordSaltStrong = "DeliberatelyInsecure1235"


try:
    md = hashlib.sha256() # creo una instancia de sha265
    salted = password + passwordSaltStrong + username
    hash = md.update(salted.encode('utf-8')) # codifico salted a UTF-8, luego lo paso por la instancia de sha265

    print(base64.b64encode(md.digest()).decode('utf-8')) # paso la cadena de bytes en caracteres legibles
except Exception as e:
    print("Error:", e)
