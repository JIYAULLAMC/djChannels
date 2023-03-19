# real time data with generic consumers 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio

class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("connected ........")
        self.accept()
     


    def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        
        for i in range(30):
            self.send(f"message from server {i}")
            sleep(1)



    def disconnect(self, close_code):
        print("disconnected .........")




class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("connected ........")
        await self.accept()
      


    async def receive( self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        
        for i in range(30):
            await self.send( text_data = f"message from server {i}")
            await asyncio.sleep(1)



    async def disconnect( self, close_code):
        print("disconnected .........")