from django.urls import path
from app import consumers
# may get error


websocket_urlpatterns = [
    path('sync/', consumers.MySyncConsumer.as_asgi),
    path('async/', consumers.MyAsyncConsumer.as_asgi()),
]

# values = ws://127.0.0.1:8000/sync
