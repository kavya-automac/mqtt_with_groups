from django.urls import path
from. import consumers


print("routingggg")
websocket_urlpatterns=[
    path('mqtt_app', consumers.ChatConsumer.as_asgi())

]



