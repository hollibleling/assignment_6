from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import ValidationError

import requests
import re

from user.models import User
from car.models import Tire

class TireListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    trimId = serializers.IntegerField()

    class Meta:
        model = Tire
        fields = ['id', 'trimId', 'user_id', 'name']
    
    def create(self, validated_data):
        name = validated_data['name']
        trimId = validated_data['trimId']
        user = User.objects.get(name = name)

        url = "https://dev.mycar.cardoc.co.kr/v1/trim/" + str(trimId)
        response = requests.get(url)
        
        frontTire = response.json()['spec']['driving']['frontTire']['value']
        rearTire = response.json()['spec']['driving']['rearTire']['value']

        tireRegex = re.compile(r'^[0-9]+/[0-9]+[a-zA-Z]+[0-9]+$')

        if not tireRegex.match(frontTire) or not tireRegex.match(rearTire):
            raise ValidationError('wrong type')

        if frontTire == '':
            frontWidth = 0
            frontRatio = 0
            frontSize = 0
            frontStruct = ''

        else:
            frontWidth = frontTire.split('/')[0]
            frontRemains = frontTire.split('/')[1]
        
            for i in ['R', 'ZR']:
                if i in frontRemains:
                    frontRemains = frontRemains.split(i)
                    struct = i
                else:
                    continue
        
            frontRatio = frontRemains[0]
            frontSize = frontRemains[1]
            frontStruct = struct

        if rearTire == '':
            rearWidth = 0
            rearRatio = 0
            rearSize = 0
            rearStruct = ''

        else:
            rearWidth = rearTire.split('/')[0]
            rearRemains = rearTire.split('/')[1]


            for i in ['R', 'ZR']:
                if i in rearRemains:
                    rearRemains = rearRemains.split(i)
                    struct = i
                else:
                    continue
            
            rearRatio = rearRemains[0]
            rearSize = rearRemains[1]
            rearStruct = struct
        with transaction.atomic():
            tireSet = Tire.objects.create(
                trimId = trimId,
                frontTire = frontTire, 
                frontWidth = frontWidth,
                frontFlatnessRatio = frontRatio,
                frontStruct = frontStruct,
                frontWheelSize = frontSize,
                rearTire = rearTire, 
                rearWidth = rearWidth,
                rearFlatnessRatio = rearRatio,
                rearStruct = rearStruct,
                rearWheelSize = rearSize,
                user_id = user.id
            )

        return tireSet

    def to_representation(self, instance):
        user_id = instance.user_id
        name = User.objects.get(id=user_id).name

        return {
            "trimId" : instance.trimId,
            "?????? ?????????" : instance.frontTire,
            "?????? ???" : instance.frontWidth, 
            "?????? ?????????" : instance.frontFlatnessRatio,
            "?????? ??????" : instance.frontStruct, 
            "?????? ???" : instance.frontWheelSize, 
            "?????? ?????????" : instance.rearTire,
            "?????? ???" : instance.rearWidth,
            "?????? ?????????" : instance.rearFlatnessRatio,
            "?????? ??????" : instance.rearStruct,
            "?????? ???" : instance.rearWheelSize,
            "?????????" : name
        }
