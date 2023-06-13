from datetime import time
from django.apps import apps

import paho.mqtt.client as mqtt
from django.conf import settings

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

print('mqtt')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        # mqtt_client.subscribe('django/mqtt')
        client.subscribe('test_data')
    else:
        print('Bad connection. Code:', rc)


def on_message(client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    # message = Message(msg=msg.payload)
    # message.save()

    # Message = apps.get_model('mqtt_app', 'Message')
    # print('apps', apps)

    payload = msg.payload.decode()  # Assuming the payload is a string
    # message = Message(msg=payload)
    #
    # message.save()

    channel_layer = get_channel_layer()#get default channel layer  RedisChannelLayer(hosts=[{'address': 'redis://65.2.3.42:6379'}])
    async_to_sync(channel_layer.group_send)("chat", {"type": "chat.message", "text": payload})


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)

client.loop_start()
