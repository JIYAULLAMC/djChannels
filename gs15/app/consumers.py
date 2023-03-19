# real time data with generic consumers 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

import json



class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("connected ........")
        print("layer is ", self.channel_layer)
        print("layer name ", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group name is ", self.group_name )
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
     
    def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        py_text_data = json.loads(text_data)
        message = py_text_data['msg']

        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type': 'chat.message',
            'message': message,
                })
    def chat_message(self, event):
        print("message from the event is ", event)
        self.send(text_data=json.dumps({
            'msg' : event['message']
        }))
        
     


    def disconnect(self, close_code):
        print("disconnected .........")
        # used to close the connection
        # self.close()
        async_to_sync(self.channel_layer.group_discard )(self.group_name, self.channel_name)




class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("connected ........")
        print("layer is ", self.channel_layer)
        print("layer name ", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group name is ", self.group_name )
        await async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        await self.accept()
     
    async def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        py_text_data = json.loads(text_data)
        message = py_text_data['msg']

        await self.channel_layer.group_send(self.group_name,{
            'type': 'chat.message',
            'message': message,
                })
    async def chat_message(self, event):
        print("message from the event is ", event)
        await self.send(text_data=json.dumps({
            'msg' : event['message']
        }))
        
     


    def disconnect(self, close_code):
        print("disconnected .........")
        # used to close the connection
        # self.close()
        async_to_sync(self.channel_layer.group_discard )(self.group_name, self.channel_name)



