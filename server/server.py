import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[SERVER] Received: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("broker", 1883)
client.subscribe("iot/sensor")
client.on_message = on_message
print("[SERVER] Waiting for messages...")
client.loop_forever()
