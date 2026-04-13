🚀 Django Channels Async WebSocket (No-Redis Version)
This project demonstrates how to implement a real-time OTP verification and multi-step notification system using Django Channels and Daphne. It uses a direct AsyncWebsocketConsumer model, which is highly efficient for 1-to-1 communication without the overhead of Redis.




1. 📥 Prerequisites & Installation
First, ensure you have Python installed. You need to install daphne and channels.
Bash
# Install Django Channels and the Daphne ASGI server
pip install daphne channels




2. ⚙️ Project Configuration (settings.py)
In your Django settings, you must register daphne and channels. Note: daphne must be placed at the very top of INSTALLED_APPS.
Python
# settings.py

INSTALLED_APPS = [
    'daphne',    # Mandatory: Must be at the top
    'channels',  # Enables WebSocket support
    'app1',      # Your application name
    # ... other apps
]

# Set the ASGI application path
ASGI_APPLICATION = 'projectchat.asgi.application'

# No CHANNEL_LAYERS (Redis) is required for this direct-response setup.





3. 🛡️ ASGI Configuration (asgi.py)
The asgi.py file acts as a router. It directs standard HTTP requests to Django and WebSocket requests to your routing.py.
Python
# projectchat/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import app1.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectchat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app1.routing.websocket_urlpatterns
        )
    ),
})





4. 🌐 Routing & Consumers
WebSocket Routing (routing.py)
Define the URL path for your WebSocket connection. Use .as_asgi() instead of .as_view().
Python
# app1/routing.py
from django.urls import path
from .consumers import LoginConsumer

websocket_urlpatterns = [
    path('ws/login/', LoginConsumer.as_asgi()),
]




Async Consumer Logic (consumers.py)
This handles the non-blocking logic. It receives an OTP and sends back two separate messages with a delay.
Python
# app1/consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class LoginConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('otp') == "1234":
            # Step 1: Send Welcome Message
            await self.send(text_data=json.dumps({'message': 'Welcome!'}))
            
            # Non-blocking delay
            await asyncio.sleep(1) 
            
            # Step 2: Send Form Request
            await self.send(text_data=json.dumps({'message': 'Please fill the form'}))




5. 💻 Client-Side Integration (Frontend)
To test the connection from a second laptop, use the Server's Local IP Address.
JavaScript
// Connect using the Server's IPv4 address
const socket = new WebSocket('ws://192.168.1.16:8000/ws/login/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    // Display as a Pop-up (Alert or SweetAlert2)
    alert(data.message);
};

function verify() {
    socket.send(JSON.stringify({"otp": "1234"}));
}




🛠️ Network & Running Instructions
Find your IP: Run ipconfig on the server machine to find your IPv4 Address.
Allowed Hosts: In settings.py, set ALLOWED_HOSTS = ['*'] or add your specific IP.
Run Server: Start the server bound to all network interfaces:
Bash
python manage.py runserver 0.0.0.0:8000




Firewall: Ensure Windows Defender Firewall is turned off or allows Port 8000 for incoming connections.

Summary: This setup is optimized for performance up to 200+ concurrent users by leveraging Python's asyncio without the complexity of a message broker like Redis.

