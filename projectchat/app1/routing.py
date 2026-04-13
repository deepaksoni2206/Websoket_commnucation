from django.urls import path
from app1.consumers import LoginConsumer

websocket_urlpatterns = [
    path('ws/login/', LoginConsumer.as_asgi()),
]