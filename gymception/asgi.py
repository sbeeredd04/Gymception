import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from members.consumers import QueueConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymception.settings')

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    path('ws/notifications/', QueueConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
