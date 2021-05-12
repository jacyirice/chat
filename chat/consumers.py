from django.shortcuts import render, redirect, get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import Group


@database_sync_to_async
def get_group(group_id, user):
    try:
        return Group.objects.get(id=group_id, members__user=user)
    except Group.DoesNotExist:
        return None

@database_sync_to_async
def send_group_messages(group, user, message, type=3):
    return group.messages.create(content=message, user=user, group=group, type=type)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_object = await get_group(self.room_name, self.user)
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        messageObj = await send_group_messages(
            group=self.group_object,
            user=self.user,
            message=message,
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'user': self.user.username,
                'type': 'chat_message',
                'message': message,
                'time': str(messageObj.date_time.time())[:8]
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        event.update({'type': 'chat_message',})
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
