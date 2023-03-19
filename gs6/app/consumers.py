
from channels.consumer import SyncConsumer, AsyncConsumer
from time import sleep
from channels.exceptions import StopConsumer
import asyncio

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("sync connect method +++++++++")
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("sync receive method +++++++++++", event)
        print("sync message ", event['text'])
        for i in range(20):    
            self.send({
                'type':"websocket.send",
                "text": f"message count{i}"
            })
            sleep(1)


    def websocket_disconnect(self, event):
        print("sync disconnect method ++++++++++++")
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("async connect method +++++++++")
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("async receive method +++++++++++", event)
        print("async message ", event['text'])
        for i in range(20):    
            await self.send({
                'type':"websocket.send",
                "text": f"message count{i}"
            })
            await asyncio.sleep(1)


    async def websocket_disconnect(self, event):
        print("async disconnect method ++++++++++++")
        raise StopConsumer()



