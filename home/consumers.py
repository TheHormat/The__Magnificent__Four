import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StudentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "students",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "students",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.channel_layer.group_send(
            "students",
            {
                'type': 'student_message',
                'message': message
            }
        )

    async def student_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))