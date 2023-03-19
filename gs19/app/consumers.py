
# real time data
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    # method called when start the connection handshake
    def connect(self):
        print("++++++++++++++++++ connected !")
        # used to accept the connection
        print("channel layer +++++++++++", self.channel_layer)
        print("channel name ++++++++++", self.channel_name)

        self.group_name = self.scope['url_route']["kwargs"]['groupkaname']
        print("gruopu name ++++++++", self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        # used to forcebally close the connection
        # self.close()

    # work when client send the message
    def receive_json(self, content, **kwargs):
        print("+++++++++++++++++++++ receive function")
        print("++++++content ", content)
        # used for sending the message to the client
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat.message",
                'message': content['msg'],
            }
        )

    def chat_message(self, event):
        print("event is ", event)
        self.send_json({
            'message': event['message'] 
        })

    # work when to disconnect the connection
    def disconnect(self, code):
        print("++++++++++++++++++++ disconnected !", code)
        print("++++++++++++++", self.channel_name)
        print("----------------", self.channel_layer)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print("++++++++++++++++++ connected !")
        print("channel layer +++++++++++", self.channel_layer)
        print("channel name ++++++++++", self.channel_name)

        self.group_name = self.scope['url_route']["kwargs"]['groupkaname']
        print("gruopu name ++++++++", self.group_name)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print("+++++++++++++++++++++ receive function")
        print("++++++content ", content)
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                'message': content['msg'],
            }
        )

    async def chat_message(self, event):
        print("event is ", event)
        await self.send_json({
            'message': event['message'] 
        })

    async def disconnect(self, code):
        print("++++++++++++++++++++ disconnected !", code)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
