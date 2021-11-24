from django.db import models
from user.models import User

class Tire(models.Model):
    trimId = models.SmallIntegerField()
    frontTire = models.CharField(max_length=32, null=True, blank=True)
    frontWidth = models.SmallIntegerField(null=True, blank=True, default=0)
    frontFlatnessRatio = models.SmallIntegerField(null=True, blank=True, default=0)
    frontStruct = models.CharField(max_length=16, null=True, blank=True)
    frontWheelSize = models.SmallIntegerField(null=True, blank=True, default=0)
    rearTire = models.CharField(max_length=32, null=True, blank=True)
    rearWidth = models.SmallIntegerField(null=True, blank=True, default=0)
    rearFlatnessRatio = models.SmallIntegerField(null=True, blank=True, default=0)
    rearStruct = models.CharField(max_length=16, null=True, blank=True)
    rearWheelSize = models.SmallIntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
