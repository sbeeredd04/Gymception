# members/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class QueueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Logic to add to a group if needed using self.scope["user"]
        await self.accept()

    async def disconnect(self, close_code):
        # Logic to remove from a group and cleanup if needed
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
