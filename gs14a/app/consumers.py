
# topic  : Generic consumer 
# real time example and how to connect with front end 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep

class MyWebSocketConsumer(WebsocketConsumer):

    def connect(self):
        print("socket connect method !++++++++++++")
        print("channel layer", self.channel_layer)
        print("channel name",  self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("groupname is ===============", self.group_name)

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("message method ++++++++++",text_data)
        # sending the real time data and its calculation

        for i in range(20):
            self.send(text_data=str(i))
            sleep(1)


    def disconnect(self, close_data):
        print("disconnect method +++++++++++")

import asyncio

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("async socket connect method !++++++++++++")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("async message method ++++++++++",text_data)

        for i in range(20):
            await self.send(text_data=str(i))
            await asyncio.sleep(1)

    async def disconnect(self, close_data):
        print("async disconnect method +++++++++++")