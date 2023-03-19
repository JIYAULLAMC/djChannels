from django.urls import path
from app import consumers


websocket_urlpatterns = [
    path("ws/sc/",consumers.MySyncConsumer.as_asgi()),
    path("ws/ac/",consumers.MyAsyncConsumer.as_asgi()),
]