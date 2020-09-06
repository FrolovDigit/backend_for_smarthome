import os, django
os.environ["DJANGO_SETTINGS_MODULE"] = 'smarthome4.settings'
django.setup()
from django.conf import settings
from smarthome.models import *
import paho.mqtt.client as mqtt
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   client.subscribe([
       ('test',2),
       ('Home/Light/LightSensor/Lux',2),
       ('Home/Light/Level',2),
       ('Home/Light/setlevel',2),
       ('Home/Light/Turner',2),
       ('Home/Access/GetPhoto',2),
       ('Home/Access/TryOpen',2),
       ('Home/Access/ReadRfid',2),
       ('Home/Access/Open',2),
       ('Home/Climate/ClimatStation/TemperatureOut',2),
       ('Home/Climate/Window/Position',2),
       ('Home/Climate/ClimatStation/Pressure',2),
       ('Home/Climate/ClimatStation/humidity',2),
       ('Home/Climate/ClimatStation/WaterLvl',2),
       ('Home/ElectricityConsumption/Energy',2)
   ])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
   # print('timestamp', msg.timestamp)
   # print('state', msg.state)
   # print('info', msg.info)
    data = str(msg.payload).rstrip("'").lstrip("b'").split(',')
    datchik = Log.objects.create()
    datchik.kanal = msg.topic
    #1ghghjgkjhhkhkjjhi
    datchik.value = data[0]
    datchik.save()
    print(data[0])
    print('payload', msg.payload)


client = mqtt.Client()
client.on_log=on_log
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('smarthome4', 'smarthome4')
client.connect('localhost')

client.loop_forever()
