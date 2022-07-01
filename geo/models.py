from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.

class Device(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, auto_created=True, unique=True)
    code = models.CharField(default="Decide Code", max_length=20, null=False, blank=False, unique=True)
    mac = models.CharField(max_length=30, blank=False, unique=True, null=False)
    package_name = models.CharField(default="Package Name", max_length=20, null=False, blank=False)

    def __str__(self):
        return self.code


class StreamSubscription(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, auto_created=True, unique=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    watchers = models.ManyToManyField(get_user_model(), )

    def get_group(self):
        return self.uid


class GeoFence(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, auto_created=True, unique=True)
    name = models.CharField(max_length=25, unique=True)
    fence = models.PolygonField(srid=4326,blank=True,null=True)

    def __str__(self):
        return self.name


class StreamMessage(models.Model):
    subscription = models.ForeignKey(StreamSubscription, on_delete=models.DO_NOTHING)
    device_uid = models.UUIDField()
    message = models.PointField(srid=4326,blank=True,default="")
    objects = models.Manager()
    date_time = models.DateTimeField()
    speed = models.CharField(default="",max_length=5, blank=True, null=True)
