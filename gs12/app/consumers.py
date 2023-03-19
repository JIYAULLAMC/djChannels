# generic consumers



from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("connected ........")
        self.accept()
        
        # used to disconnect the connection
        # self.close() 


    def receive(self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        # self.send(text_data="message from server !")

        # sending the binary data
        # data = True
        # self.send(bytes_data=data)

        # close the connection
        # self.close()

        # close connection with closing code
        self.close(code=1231)




    def disconnect(self, close_code):
        print("disconnected .........")




class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("connected ........")
        await self.accept()
        
        # used to disconnect the connection
        #  await self.close() 


    async def receive( self, text_data=None, bytes_data=None):
        print("message received .....", text_data)
        
        await self.send(text_data="message from server !")

        # sending the binary data
        # data = True
        #  await self.send(bytes_data=data)

        # close the connection
        #  await self.close()

        # close connection with closing code
        # await self.close(code=1231)




    async def disconnect( self, close_code):
        print("disconnected .........")