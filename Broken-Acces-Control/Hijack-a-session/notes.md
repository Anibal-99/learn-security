# Notas para realizar el ejercicio A1 Broken Access control
Debemos trabajar con Burpsuite.

1- Encontrar un endpoint que realice el inicio de sesion que se muestra en la seccion, lo que vendria siendo un metodo HTTP que sea un POST, para realizar el inicio.

2- Luego una ves que encontramos el metodo POST que contiene el **hijack_cookie** debemos borrar el hijack_cookie del cuerpo de la request, luego pasar al **Repeater** para solicitarle al servidor otra hijack_cookie y poder analizar que es lo que pasa.

3- Estando en el repeater debemos enviar varias peticiones y ver que pasa en cada hijack_cookie que nos devuelve el servidor.
- 83796448628260302**84**-1681415203801
- 83796448628260302**86**-1681415533460
- 83796448628260302**88**-1681415544408
- 8379644862826030290-1681415555489
- 8379644862826030291-1681415581508
- 8379644862826030292-1681415594056
- 83796448628260302**93**-1681415602097
- 83796448628260302**95**-1681415690519

Todos estos son valores que nos devuelve el servidor. sobre el hijack_cookie.

4- como se puede ver en cada valor de los numeros en negrita, se puede ver que en cada par/dos solicitudes los numero aumentan de 2 en 2, esto quiere decir que entre esas dos solicitudes otro usuario inicio sesion.

5- Una vez analizado lo que nos devuelve el servidor ya podemos obtener el numero de sesion de otro usuario. Lo que no se es lo que viene despues del valor del session_id, que es un timestamp (marca temporal) de unix.
