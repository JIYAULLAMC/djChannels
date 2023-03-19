# chat app on saving the data

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat
from channels.db import database_sync_to_async


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("connected ........")
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
     
    def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        py_text_data = json.loads(text_data)
        
        message = py_text_data['msg']
        group = Group.objects.get(name=self.group_name)   
        if self.scope['user'].is_authenticated:
            chat_obj = Chat(content= message, group=group)
            chat_obj.save()  

            async_to_sync(self.channel_layer.group_send)(self.group_name,{
                'type': 'chat.message',
                'message': message,
                    })
            
        else:
            self.send(text_data=json.dumps({
                'msg' : "Login Required!"
            }))
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
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
     
    async def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        py_text_data = json.loads(text_data)
        message = py_text_data['msg']

        if self.scope['user'].is_authenticated:
            group = await database_sync_to_async(Group.objects.get)(name=self.group_name)   
            chat_obj = Chat(content= message, group=group)
            await database_sync_to_async(chat_obj.save)()  

            await self.channel_layer.group_send(self.group_name,{ 
                'type': 'chat.message',
                'message': message,
                    })              
        else:
            self.send(text_data=json.dumps({
                'msg' : "Login Required!"
            }))

    async def chat_message(self, event):
        print("message from the event is ", event)
        await self.send(text_data=json.dumps({
            'msg' : event['message']
        }))

        
    
    async def disconnect(self, close_code):
        print("disconnected .........")
        # used to close the connection
        # self.close()
        async_to_sync(self.channel_layer.group_discard )(self.group_name, self.channel_name)


