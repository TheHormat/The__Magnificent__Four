from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/students/', consumers.StudentConsumer.as_asgi()),
]