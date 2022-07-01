from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.status import *
from rest_framework.permissions import (AllowAny, IsAuthenticated)

from .models import *
from .serializers import *


class IndexView(APIView):
    @permission_classes((AllowAny,))
    def get(self, request, uid=None):
        if uid is None:
            return Response({"path": '/geo'})
        if not Device.objects.filter(uid=uid).exists():
            return Response(status=HTTP_404_NOT_FOUND)
        device = Device.objects.get(uid=uid)
        serializer = DeviceSerializer(instance=device)
        return Response(serializer.data)

    @permission_classes((IsAuthenticated,))
    def post(self, request):
        serializer = DeviceSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
