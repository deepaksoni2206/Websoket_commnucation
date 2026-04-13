# import json
# from channels.generic.websocket import WebsocketConsumer
# import time 


# check sync 

# class LoginConsumer(WebsocketConsumer):
#     def connect(self):
#         # Connection accept karo
#         self.accept()
#         print("Connection established!")

#     def disconnect(self, close_code):
#         print("Disconnected!")

#     def receive(self, text_data):
#         # User se data receive karna
#         data = json.loads(text_data)
#         otp = data.get('otp')
        
#         # Simple Logic: OTP check aur usi user ko reply
#         if otp == "1234":
#             response_msg = "OTP Verified! Welcome to the Dashboard."
#         else:
#             response_msg = "Invalid OTP. Please try again."

#         # Sirf isi user ko wapas message bhejna (No Redis involved)
#         for i in range(50):
#             time.sleep(1)  # 1 second delay
#             self.send(text_data=json.dumps({
#                 'message': i
#             }))





# just check with time 


# import json
# import asyncio # Time delay ya async tasks ke liye
# from channels.generic.websocket import AsyncWebsocketConsumer

# from projectchat.app1 import models

# class LoginConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Connection accept karna (Async mein await zaroori hai)
#         await self.accept()
#         print("Connected asynchronously!")

#     async def disconnect(self, close_code):
#         print(f"Disconnected with code: {close_code}")

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         otp = data.get('otp')

#         if otp == "1234":
#             # 1. Pehla message: Welcome
#             for i in range(50):
#                 await asyncio.sleep(1)  # 1 second delay
#                 await self.send(text_data=json.dumps({
#                     'type': 'welcome',
#                     'message': f"Welcome! This is message number {i+1}."
#                 }))
            # await self.send(text_data=json.dumps({
            #     'type': 'welcome',
            #     'message': "OTP Verified! Welcome to the system."
            # }))

            # Chota sa delay (optional) taaki user ko feel ho ki process ho raha hai
            # Bina block kiye wait karega kyunki ye 'await' hai
            # await asyncio.sleep(1) 

            # # 2. Doosra message: Form Message
            # await self.send(text_data=json.dumps({
            #     'type': 'form_request',
            #     'message': "Please fill out your profile details.",
            #     'fields': ['Full Name', 'City', 'Experience']
            # }))
            
        # else:
        #     await self.send(text_data=json.dumps({
        #         'type': 'error',
        #         'message': "Invalid OTP. Try again."
        #     }))


import json
import asyncio # Time delay ya async tasks ke liye
from channels.generic.websocket import AsyncWebsocketConsumer

class LoginConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connection accept karna (Async mein await zaroori hai)
        await self.accept()
        print("Connected asynchronously!")

    async def disconnect(self, close_code):
        print(f"Disconnected with code: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        otp = data.get('otp')

        if otp == "1234":
            # 1. Pehla message: Welcome
            await self.send(text_data=json.dumps({
                'type': 'welcome',
                'message': "OTP Verified! Welcome to the system."
            }))

            # Bina block kiye wait karega kyunki ye 'await' hai
            await asyncio.sleep(1) 

            # 2. Doosra message: Form Message
            await self.send(text_data=json.dumps({
                'type': 'form_request',
                'message': "Please fill out your profile details.",
                'fields': ['Full Name', 'City', 'Experience']
            }))
            
        else:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': "Invalid OTP. Try again."
            }))





#     # for database check
# # models.py
# class UserOTP(models.Model):
#     phone = models.CharField(max_length=15, db_index=True)
#     otp = models.CharField(max_length=6)
#     is_verified = models.BooleanField(default=False)
    
    
# import json
# import asyncio
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async 
# from .models import UserOTP # Maan lijiye aapka model yahan hai

# class LoginConsumer(AsyncWebsocketConsumer):
    
#     # 1. Connection Method
#     async def connect(self):
#         # Jab user connect karega
#         await self.accept()
#         print("WebSocket Connected and Waiting for OTP...")

#     # 2. Disconnect Method
#     async def disconnect(self, close_code):
#         # Jab user tab ya browser band karega
#         print(f"WebSocket Disconnected: {close_code}")

#     # 3. Database Helper Method (Sync to Async bridge)
#     @database_sync_to_async
#     def verify_otp_from_db(self, user_phone, user_otp):
#         try:
#             # MySQL mein check karna (Index hona zaroori hai phone par)
#             return UserOTP.objects.filter(phone=user_phone, otp=user_otp).exists()
#         except Exception as e:
#             print(f"DB Error: {e}")
#             return False

#     # 4. Receive Method (Main Logic)
#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         user_otp = data.get('otp')
#         user_phone = data.get('phone')

#         # Database se check karwao
#         is_valid = await self.verify_otp_from_db(user_phone, user_otp)

#         if is_valid:
#             # Pehla message: Success Pop-up
#             await self.send(text_data=json.dumps({
#                 'type': 'welcome',
#                 'message': "OTP Verified! Welcome to the system."
#             }))

#             await asyncio.sleep(1) # Chota pause professional feel ke liye

#             # Doosra message: Form Pop-up
#             await self.send(text_data=json.dumps({
#                 'type': 'form_request',
#                 'message': "Please fill out your profile details.",
#                 'fields': ['Full Name', 'City', 'Experience']
#             }))
            
#         else:
#             # Error message
#             await self.send(text_data=json.dumps({
#                 'type': 'error',
#                 'message': "Invalid OTP or Phone. Please try again."
#             }))