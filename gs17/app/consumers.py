

from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer



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
        self.send_json({"message": "message from server !"})

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
        await self.send_json({"message": "message from server !"})

    async def disconnect(self, code):
        print("++++++++++++++++++++ disconnected !", code)
