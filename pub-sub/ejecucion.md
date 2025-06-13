# Guia de uso

## 1. Ejecutar *broker*

Abre una terminal(*cmd*)

~~~bash
python broker.py
~~~

Se mostrara como resultado:

~~~bash
[BROKER] Escuchando en 0.0.0.0:14000...
~~~

## 2. Ejecutar uno o mas subscriptores
Abre una terminal y ejecuta un subscriptor o mas

~~~bash
python subscriber.py
~~~

Cuando se te pida, escribe el tema (*topic*),por ejemplo:
~~~bash
Tema a suscribirse: deportes
~~~

El sistema mantendra la conexion abierta esperando mensajes del *broker*

## 3. Ejecuta uno o mas publicadores

~~~bash
python publisher.py
~~~

Envia un mensaje en este formato:

~~~bash
deportes: ¡El america gano 15-0!
~~~

Todos los *suscriptores* suscritos a *deportes* recibiran:

~~~bash
[deportes] ¡El pumas gano 5-0!
~~~