from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print(" SyncConsumer Web socket Connect ++++++++++++++++!", event)
        self.send({
            "type":"websocket.accept",
        })

    def websocket_receive(self, event):
        print(" SyncConsumermessage received from client ++++++++++",event)
        print(event["text"])
        self.send({
            "type": "websocket.send",
            "text": "SyncConsumer message is send to sever!"
        })

    def websocket_disconnected(self, event):
        print(" SyncConsumer disconnected! ++++++++++++++", event)
        raise StopConsumer() 


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print(" AsyncConsumer Web socket Connect ++++++++++++++++!", event)
        await self.send({
            "type":"websocket.accept",
        })

    async def websocket_receive(self, event):
        print(" AsyncConsumer message received from client ++++++++++",event)
        print(event["text"])
        await self.send({
            "type": "websocket.send",
            "text": " AsyncConsumer message is send to sever!"
        })

    async def websocket_disconnected(self, event):
        print(" AsyncConsumer disconnected! ++++++++++++++", event)
        raise StopConsumer() 
    


a = 10

