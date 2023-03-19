from django.urls import path
from app import consumers


websocket_urlpatterns = [
    path("ws/wsc/<str:groupname>/", consumers.MyWebSocketConsumer.as_asgi()),
    path("ws/awsc/<str:groupname>/", consumers.MyAsyncWebsocketConsumer.as_asgi()),
]