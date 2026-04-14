"""
ASGI config for projectchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectchat.settings')

# application = get_asgi_application()




# projectchat/asgi.py

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# import app1.routing 

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectchat.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             app1.routing.websocket_urlpatterns
#         )
#     ),
# })

from projectchat import app1
import projectchat.app1.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectchat.projectchat.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            projectchat.app1.routing.websocket_urlpatterns
        )
    ),
})