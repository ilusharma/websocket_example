# routing.py

from django.urls import path
from .consumers import GetPriceConsumer

websocket_urlpatterns = [
    path('ws/get_price/', GetPriceConsumer.as_asgi()),
]
