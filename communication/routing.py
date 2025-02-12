from django.urls import path
from communication.consumers import ChatConsumer  # Ensure this exists


websocket_urlpatterns = [
    path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
]
