from channels.generic.websocket import AsyncWebsocketConsumer
import json

class QueueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add the connected user to a group to receive notifications
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove user from the group on disconnect
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def receive(self, text_data):
        # Handle incoming data (if needed, mostly you'll send only from server to client)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

    async def send_notification(self, event):
        # Send the actual notification to WebSocket
        message = event['message']  # Contains HTML or notification content
        await self.send(text_data=json.dumps({
            'message': message
        }))
        
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class WorkoutConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

