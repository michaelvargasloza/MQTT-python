import paho.mqtt.client as mqtt

# La devolución de llamada para cuando el cliente recibe una respuesta CONNACK del servidor.
def on_connect(client, userdata, flags, rc):
    print("Se conectó con MQTT " + str(rc))

    # Suscribirse en on_connect() significa que si perdemos la conexión y
    # vuelva a conectarse y se renovarán las suscripciones.
    client.subscribe("ALSW/#")
    # Instalar mosquitto
    # Mensaje de prueba: mosquitto_pub -h test.mosquitto.org -t "ALSW/" -m "69"
    # Mensaje de prueba (temp): mosquitto_pub -h test.mosquitto.org -t "ALSW/temp" -m "98"

# La devolución de llamada para cuando se recibe un mensaje PUBLICAR del servidor.
def on_message(client, userdata, msg):
    if msg.topic == "ALSW/temp":
        print(f"Temperatura es {str(msg.payload)}")
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Bloqueo de llamadas que procesa el tráfico de la red, envía devoluciones de llamadas y
# maneja la reconexión.
# Hay otras funciones loop*() disponibles que brindan una interfaz roscada y una
# interfaz manual.
client.loop_forever()