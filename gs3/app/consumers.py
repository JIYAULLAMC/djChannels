
from channels.consumer import SyncConsumer, AsyncConsumer



class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('Sync Connected +++++++++++++++++++++')
        self.send({'type':'websocket.accept'})

    def websocket_receive(self, event):
        print('Sync received +++++++++++++++++++++', event['text'])
        self.send({
            'type':'websocket.send',
            'text': 'message sent to the client!'
        })

    def websocket_disconnect(self, event):
        print('Sync Disconnected +++++++++++++++++++++')


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('Async Connected +++++++++++++++++++++')

    async def websocket_receive(self, event):
        print('Async received +++++++++++++++++++++')

    async def websocket_disconnect(self, event):
        print('Async Disconnected +++++++++++++++++++++')


