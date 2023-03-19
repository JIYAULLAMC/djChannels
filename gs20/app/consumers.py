
# real time data
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync
from .models import Group, Chat
from channels.db import database_sync_to_async

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
        group = Group.objects.get(name=self.group_name)
        chat = Chat(content= content['msg'], group= group)
        chat.save()

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
        
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        chat = Chat(content= content['msg'], group= group)
        await database_sync_to_async(chat.save)()

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
