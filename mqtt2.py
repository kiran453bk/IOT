import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "iot/demo/temp"

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER)
client.subscribe(TOPIC)

print("Subscribed... waiting for messages.")
client.loop_forever()