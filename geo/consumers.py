from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class GeoConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.accept())
        async_to_sync(self.send(text_data=json.dumps({"status": "Accepted"})))

    def receive(self, message):
        print(message)
        async_to_sync(self.send(text_data=json.dumps({"status": "Received", "message": message})))