import paho.mqtt.client as mqtt
import random
import time

BROKER = "test.mosquitto.org"
TOPIC = "iot/demo/temp"

client = mqtt.Client()
client.connect(BROKER)

print("Publishing temperature data...")

while True:
    temp = round(25 + random.uniform(-2, 2), 2)
    message = f"{temp}"
    
    client.publish(TOPIC, message)
    print("Sent:", message)

    time.sleep(1)

