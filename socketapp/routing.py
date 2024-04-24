# routing.py

from django.urls import path
from .consumers import GetPriceConsumer,ChatBotConsumer

websocket_urlpatterns = [
    path('ws/get_price/', GetPriceConsumer.as_asgi()),
    path('ws/chat/', ChatBotConsumer.as_asgi()),

]
