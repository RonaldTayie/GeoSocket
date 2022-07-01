from rest_framework import serializers
from .models import *


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class StreamSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamSubscription
        fields = '__all__'


class GeoFenceSerializer(serializers.ModelSerializer):
    class Meta:
        models = GeoFence
        fields = '__all__'


class StreamMessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = StreamMessage
        fields = '__all__'
