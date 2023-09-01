import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to broker")
        global Connected 
        Connected = True
        
    else:
        print("connection failed")
        
        
Connected = False

client = mqtt.Client()
client.on_connect = on_connect
client.connect("197.255.72.34", 1883, 60)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
    
try:
    while True:
        message = input('message')
        client.publish("glblcd/ourMQTT")
        
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
    