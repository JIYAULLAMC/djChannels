import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from app.routing import websocket_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs16.settings")


# application =  ProtocolTypeRouter({
#     "http" : get_asgi_application(),
#     'websocket': URLRouter(websocket_urlpatterns),
# })

# for authentications user the middleware
from channels.auth import AuthMiddlewareStack
application = AuthMiddlewareStack( ProtocolTypeRouter({
    "http" : get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
}))
