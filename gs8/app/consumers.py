from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

class MySyncConsumer(SyncConsumer):


    def websocket_connect(self, event):
        print("sync connect method ! 10+++++++++++",event)
        # default channel from the project 
        print("layer object 12-------------", self.channel_layer)
        # get channel name
        print("layer name 14-------------", self.channel_name)
        # createing and adding in the group
        async_to_sync(self.channel_layer.group_add)('programmers', self.channel_name)

        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("sync event method ! 23+++++++++++",event)
        print("sync message  ! 24+++++++++++",event['text'])
        print("sync message type ! 25+++++++++++", type(event['text']))
    
        async_to_sync(self.channel_layer.group_send)('programmers',{
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print("event 33-------", event, type(event))
        print("message 34-------", event['message'])
        print("actual data 35-------", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })


    def websocket_disconnect(self, event):
        print("sync disconnect method ! 43+++++++++++",event)
        # channel layer
        print("layer object 45-------------", self.channel_layer)
        # get channel name
        print("layer name 47-------------", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('programmers', self.channel_name)
        # createing and adding in the group
        raise StopConsumer()



class MyAsyncConsumer(AsyncConsumer):


    async def websocket_connect(self, event):
        print("sync connect method ! 10+++++++++++",event)
        # default channel from the project 
        print("layer object 12-------------", self.channel_layer)
        # get channel name
        print("layer name 14-------------", self.channel_name)
        # createing and adding in the group
        await self.channel_layer.group_add ('programmers', self.channel_name)

        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("sync event method ! 23+++++++++++",event)
        print("sync message  ! 24+++++++++++",event['text'])
        print("sync message type ! 25+++++++++++", type(event['text']))
    
        await self.channel_layer.group_send('programmers',{
            'type': 'chat.message',
            'message': event['text']
        })

    async def chat_message(self, event):
        print("event 33-------", event, type(event))
        print("message 34-------", event['message'])
        print("actual data 35-------", type(event['message']))
        await self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })


    async def websocket_disconnect(self, event):
        print("sync disconnect method ! 43+++++++++++",event)
        # channel layer
        print("layer object 45-------------", self.channel_layer)
        # get channel name
        print("layer name 47-------------", self.channel_name)
        await self.channel_layer.group_discard ('programmers', self.channel_name)
        # createing and adding in the group
        raise StopConsumer()