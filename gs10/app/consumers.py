from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from app.models import Group, Chat
from channels.db import database_sync_to_async

class MySyncConsumer(SyncConsumer):


    def websocket_connect(self, event):
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):    
        python_data = json.loads(event['text'])
        print("python data and type is +++++++ ", python_data, type(python_data))
        message = python_data['msg']
        print("message ++++++++++", message, type(message))

        group = Group.objects.filter(name=self.group_name).first()

        chat = Chat(content=message, group=group)
        chat.save()
         
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })


    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        # createing and adding in the group
        raise StopConsumer()



class MyAsyncConsumer(AsyncConsumer):


    async def websocket_connect(self, event):
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add (self.group_name, self.channel_name)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        
        python_data = json.loads(event['text'])
        print("python data and type is +++++++ ", python_data, type(python_data))
        message = python_data['msg']
        print("message ++++++++++", message, type(message))

        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)

        chat = Chat(content=message, group=group)
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(self.group_name,{
            'type': 'chat.message',
            'message': event['text']
        })

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })


    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard (self.group_name, self.channel_name)
        # createing and adding in the group
        raise StopConsumer()