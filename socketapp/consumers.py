# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests

#example for sending message using server side
class GetPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "price_updates"  # Define the group name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # This consumer doesn't handle receiving messages from clients,
        # it's used to broadcast messages to clients.
        pass

    async def send_price(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            'message': message
        }))



#sending message using client side

class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name ="chat"
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    async def receive(self,text_data):
        print(text_data)
        data = json.loads(text_data)

        # Extract the user message from the received data
        user_message = data.get('message')
        #handle recived data

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat_message',
                'message':user_message
            }
        )

    async def chat_message(self,event):
        message = event['message']


        await self.send(text_data=json.dumps({
            'message':message
        }))
