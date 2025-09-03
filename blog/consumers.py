# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# ONLINE_USERS = set()

# class StatusConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.username = self.scope["url_route"]["kwargs"]["username"]
#         ONLINE_USERS.add(self.username)
#         await self.accept()
#         # broadcast to others
#         await self.channel_layer.group_send(
#             "online_group",
#             {"type": "user_status", "user": self.username, "status": "online"}
#         )

#     async def disconnect(self, close_code):
#         if self.username in ONLINE_USERS:
#             ONLINE_USERS.remove(self.username)
#         await self.channel_layer.group_send(
#             "online_group",
#             {"type": "user_status", "user": self.username, "status": "offline"}
#         )

#     async def receive(self, text_data):
#         pass  # not needed for now

#     async def user_status(self, event):
#         await self.send(text_data=json.dumps(event))



# from channels.generic.websocket import AsyncWebsocketConsumer

# online_users = set()  # store online user IDs

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user = self.scope["user"]
#         online_users.add(self.user.id)  # mark user as online
#         await self.accept()

#     async def disconnect(self, close_code):
#         online_users.discard(self.user.id)  # mark offline



# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# online_users = {}  # store active connections

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.username = self.scope["url_route"]["kwargs"]["username"]
#         online_users[self.username] = self.channel_name
#         await self.accept()

#     async def disconnect(self, close_code):
#         if self.username in online_users:
#             del online_users[self.username]

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         receiver = data["to"]
#         message = data["message"]

#         # Only send if receiver is online
#         if receiver in online_users:
#             await self.channel_layer.send(
#                 online_users[receiver],
#                 {
#                     "type": "chat.message",
#                     "message": message,
#                     "from": self.username
#                 }
#             )

#     async def chat_message(self, event):
#         await self.send(text_data=json.dumps({
#             "from": event["from"],
#             "message": event["message"]
#         }))
