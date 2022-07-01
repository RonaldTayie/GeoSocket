from django.urls import re_path
from .consumers import GeoConsumer

websocket_urlpatterns = [
    re_path('', GeoConsumer.as_asgi())
]
