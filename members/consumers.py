from channels.generic.websocket import AsyncWebsocketConsumer
import json

class QueueConsumer(AsyncWebsocketConsumer):
    """
    This consumer handles WebSocket connections for sending real-time queue notifications.
    """
    async def connect(self):
        # Add the connected user to a group to receive notifications
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove user from the group on disconnect
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        # This method can be omitted if you don't expect to receive messages from WebSocket
        if text_data:
            try:
                text_data_json = json.loads(text_data)
                message = text_data_json.get('message')
                # You could add functionality here to process received messages
            except json.JSONDecodeError:
                pass  # handle errors or log invalid json

    async def send_notification(self, event):
        """
        Receives a message from the group and sends it out to the WebSocket.
        """
        message = event['message']  # Contains HTML or notification content
        await self.send(text_data=json.dumps({'message': message}))

class WorkoutConsumer(AsyncWebsocketConsumer):
    """
    This consumer might be used for handling real-time workout data or commands.
    """
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Cleanup or resource release can be handled here if necessary
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            try:
                text_data_json = json.loads(text_data)
                message = text_data_json['message']
                # Logic for received message
                await self.send(text_data=json.dumps({'message': message}))
            except json.JSONDecodeError:
                pass  # handle errors or log invalid json
