PROTOCOLO MQTT

Links:
- 7 Alternativas para APIs REST: https://www.pubnub.com/blog/7-alternatives-to-rest-apis/
- MQTT: el estándar para mensajería de IoT: https://mqtt.org/
- La mejor herramienta IOT | Que es MQTT: https://www.youtube.com/watch?v=T1_w8-8Y5kc
- Aprende a usar Mosquitto_Sub y Mosquitto_Pub para conectar a MQTT: https://www.youtube.com/watch?v=O10JqPeC5SA
- Ejemplo MQTT Python tutorial español: https://www.youtube.com/watch?v=T362losqJys


MQTT:

MQTT (Message Queuing Telemetry Transport - Transporte de telemetría de colas de mensajes) es un protocolo de red ligero, de publicación y suscripción, de máquina a máquina (Machine to Machine - M2M) para cola de mensajes/servicio de cola de mensajes. Está diseñado para conexiones con ubicaciones remotas que tienen dispositivos con restricciones de recursos o ancho de banda de red limitado, como en el Internet de las cosas.

Bróker:

Un bróker es el servidor con el que se comunican los clientes: recibe comunicaciones de unos y se las envía a otros. Los clientes no se comunican directamente entre sí, sino que se conectan con el bróker.

Tópico:

Los Broker MQTT aplican un filtrado a los mensajes que son recibidos desde los publicadores, para discriminar a que clientes suscritos es entregado. Este filtro se denomina Topic, y simplemente consiste en una cadena de texto UTF-8, y una longitud máxima de 65536 caracteres (aunque lo normal es que sea mucho menor). Se distingue entre mayúsculas y minúsculas.
Ejemplo:
- Casa/Cocina/Temperatura
- Casa/Salon/Temperatura
- Casa/Salon/Persiana

Recordamos que MQTT es un servicio de mensajería con patrón publicador/suscriptor (pub-sub) que funciona sobre TCP/IP, es decir, un servidor central, que en MQTT se denomina Broker, recibe los mensajes, los filtra y los distribuye a los clientes.

Mosquitto:

Eclipse Mosquitto es un intermediario de mensajes de código abierto (con licencia EPL/EDL) que implementa las versiones 5.0, 3.1.1 y 3.1 del protocolo MQTT. Mosquitto es liviano y adecuado para su uso en todos los dispositivos, desde computadoras de placa única de bajo consumo hasta servidores completos.

https://mosquitto.org/download/

Python:

paho-mqtt 1.6.1

https://pypi.org/project/paho-mqtt/
