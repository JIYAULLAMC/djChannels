
# real time data
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from time import sleep
import asyncio


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    # method called when start the connection handshake
    def connect(self):
        print("++++++++++++++++++ connected !")
        # used to accept the connection
        self.accept()
        # used to forcebally close the connection
        # self.close()

    # work when client send the message
    def receive_json(self, content, **kwargs):
        print("+++++++++++++++++++++ receive function")
        print("++++++content ", content)
        # used for sending the message to the client

        for i in range(20):
            self.send_json({"message": str(i)})
            sleep(1)

    # work when to disconnect the connection
    def disconnect(self, code):
        print("++++++++++++++++++++ disconnected !", code)



class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print("++++++++++++++++++ connected !")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print("+++++++++++++++++++++ receive function")
        print("++++++content ", content)
        for i in range(20):
            await self.send_json({"message": str(i)})
            await asyncio.sleep(1)

    async def disconnect(self, code):
        print("++++++++++++++++++++ disconnected !", code)
