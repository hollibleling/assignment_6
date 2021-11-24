from rest_framework import serializers
from rest_framework.validators import ValidationError

import requests

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
        user = self.context['request'].user

        if name != user.name:
            raise ValidationError('wrong request')

        url = "https://dev.mycar.cardoc.co.kr/v1/trim/" + str(trimId)
        response = requests.get(url)
        
        frontTire = response.json()['spec']['driving']['frontTire']['value']
        frontWidth = frontTire.split('/')[0]
        frontRemains = frontTire.split('/')[1]
        rearTire = response.json()['spec']['driving']['rearTire']['value']
        rearWidth = rearTire.split('/')[0]
        rearRemains = rearTire.split('/')[1]
        
        for i in ['R', 'ZR']:
            if i in frontRemains:
                frontRemains = frontRemains.split(i)
                struct = i
            else:
                continue
        
        frontRatio = frontRemains[0]
        frontSize = frontRemains[1]
        frontStruct = struct

        for i in ['R', 'ZR']:
            if i in rearRemains:
                rearRemains = rearRemains.split(i)
                struct = i
            else:
                continue
        
        rearRatio = rearRemains[0]
        rearSize = rearRemains[1]
        rearStruct = struct

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
        user_id = self.context['request'].user.id
        name = User.objects.get(id=user_id).name

        return {
            "trimId" : instance.trimId,
            "전륜 타이어" : instance.frontTire,
            "전륜 폭" : instance.frontWidth, 
            "전륜 편평비" : instance.frontFlatnessRatio,
            "전륜 구조" : instance.frontStruct, 
            "전륜 휠" : instance.frontWheelSize, 
            "후륜 타이어" : instance.rearTire,
            "후륜 폭" : instance.rearWidth,
            "후륜 편평비" : instance.rearFlatnessRatio,
            "후륜 구조" : instance.rearStruct,
            "후륜 휠" : instance.rearWheelSize,
            "고객명" : name
        }