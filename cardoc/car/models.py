from django.db import models
from user.models import User

class Tire(models.Model):
    trimId = models.SmallIntegerField()
    frontTire = models.CharField(max_length=32)
    frontWidth = models.SmallIntegerField()
    frontFlatnessRatio = models.SmallIntegerField()
    frontStruct = models.CharField(max_length=16)
    frontWheelSize = models.SmallIntegerField()
    rearTire = models.CharField(max_length=32)
    rearWidth = models.SmallIntegerField()
    rearFlatnessRatio = models.SmallIntegerField()
    rearStruct = models.CharField(max_length=16)
    rearWheelSize = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
