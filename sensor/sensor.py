import paho.mqtt.client as mqtt
import time, random

client = mqtt.Client()
client.connect("broker", 1883)

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)
    client.publish("iot/sensor", f"Temperature: {temperature}C")
    print(f"[SENSOR] Sent: {temperature}C")
    time.sleep(3)
