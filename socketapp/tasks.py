# tasks.py

from celery import shared_task
import requests
from .consumers import GetPriceConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random

@shared_task
def get_price():
    #random list of prices
    prices = [random.randint(1, 100) for i in range(10)]


    channel_layer = get_channel_layer()
    print("Channel Layer: ", channel_layer)
    # Construct the message to send
    message = {
        "type": "send_price",
        "message": prices,
    }
    # Send the message to the consumer
    async_to_sync(channel_layer.group_send)("price_updates", message)
    return 'Price sent!'
