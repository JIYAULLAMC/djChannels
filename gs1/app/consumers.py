from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("sync web socket is connected.. +++++++++++++++++")
        self.send({
            "type":"websocket.accept",
        })

    def websocket_receive(self, event):
        print("sync message received +++++++++++++++++.")


    def websocket_disconnect(self, event):
        print("sync web socket is disconnected +++++++++++++++++")
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("async web socket is connected +++++++++++++++++..")
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("async message received +++++++++++++++++.")


    async def websocket_disconnect(self, event):
        print("async web socket is disconnected +++++++++++++++++")
    