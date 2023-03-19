from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
    string = ""

    def websocket_connect(self, event):
        print(f"Sync websocket connect method {self.string}")
        self.send({
            'type': "websocket.accept",
        })
        self.string = self.string + ' ++'
        
    def websocket_receive(self, event):
        print(f"Sync websocket receive method {self.string} ")
        # self.send({
        #     'type': "websocket.send",
        #     'text': f"message from server{self.string}"
        # })
        # self.string = self.string + ' ++'

        ######## real time application #######
        for num in range(50):
            self.send({
                'type':"websocket.send",
                "text": str(num)
            })
            sleep(1)


    def websocket_disconnect(self, event):
        print(f"Sync websocket connect method {self.string} ")
        self.string = self.string + ' ++'

        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    string = "--"

    async def websocket_connect(self, event):
        print(f"Sync websocket connect method {self.string}")

        await self.send({
            'type': "websocket.accept",
        })
        self.string += " --"

    async def websocket_receive(self, event):
        print(f"Sync websocket connect method {self.string}")
        # await self.send({
        #     'type': "websocket.send",
        #     'text': f"message from server {self.string}"
        # })
        # self.string += " --"

        for num in range(50):
            await self.send({
                'type': "websocket.send",
                "text" : str(num)
            })
            await asyncio.sleep(1)


    async def websocket_disconnect(self, event):
        print(f"Sync websocket connect method {self.string}")
        self.string += " --"
        raise StopConsumer()
     