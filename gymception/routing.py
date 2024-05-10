from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from members.consumers import QueueConsumer, WorkoutConsumer

# Define WebSocket URL patterns
websocket_urlpatterns = [
    re_path(r'^ws/queue/$', QueueConsumer.as_asgi(), name='queue'),
    re_path(r'^ws/workouts/$', WorkoutConsumer.as_asgi(), name='workouts'),
]

application = ProtocolTypeRouter({
    # HTTP->Django views is added by default
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
