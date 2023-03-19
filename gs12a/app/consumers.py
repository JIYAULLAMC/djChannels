
# topic  : Generic consumer 

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebSocketConsumer(WebsocketConsumer):

    # will called when the connection is open and about finishe the handshake connection
    def connect(self):
        print("socket connect method !++++++++++++")
        # to accept the connection
        self.accept()
        # used to disconnect or close the connection (force fully disconnect the connections)
        # self.close() 

    # will colled when the data is received from the client
    def receive(self, text_data=None, bytes_data=None):
        print("message method ++++++++++",text_data)

        # to send the data from server to the client
        self.send(text_data="Message from sever ++++++++++")


        # used to send the binary form of data
        # self.send(bytes_data="bytes data")
        # used to disconnect or close the connection (force fully disconnect the connections)
        # self.close()  # self.close(code=1234) 

    # called when the connection is about to lost, either from server or client or some error
    def disconnect(self, close_data):
        print("disconnect method +++++++++++")


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    # will called when the connection is open and about finishe the handshake connection
    async def connect(self):
        print("async socket connect method !++++++++++++")
        # to accept the connection
        await self.accept()
        # used to disconnect or close the connection (force fully disconnect the connections)
        # await self.close() 

    # will colled when the data is received from the client
    async def receive(self, text_data=None, bytes_data=None):
        print("async message method ++++++++++",text_data)

        # to send the data from server to the client
        await self.send(text_data="async Message from sever ++++++++++")

        # used to send the binary form of data
        # await self.send(bytes_data="bytes data")
        # used to disconnect or close the connection (force fully disconnect the connections)
        # await self.close()  # await self.close(code=1234) 

    # called when the connection is about to lost, either from server or client or some error
    async def disconnect(self, close_data):
        print("async disconnect method +++++++++++")