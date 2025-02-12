# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from communication.routing import websocket_urlpatterns

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": URLRouter(websocket_urlpatterns),
#     }
# )
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from communication.routing import websocket_urlpatterns  # Ensure this exists
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(  # Wrap WebSocket with Auth Middleware
            URLRouter(websocket_urlpatterns)
        ),
    }
)
