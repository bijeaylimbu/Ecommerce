from rest_framework import serializers
from .models import  MobileCharger,Headphone,Categories


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Categories

class MobileChargerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MobileCharger

class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Headphone


