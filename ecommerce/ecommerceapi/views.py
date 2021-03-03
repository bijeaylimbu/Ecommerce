from django.shortcuts import render
from .models import Categories,MobileCharger,Headphone
from .serializers import  CategorySerialzer,MobileChargerSerializer,HeadphoneSerializer
# Create your views here.

from rest_framework import generics

class ListCategory(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerialzer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerialzer

class ListMobileCharger(generics.ListCreateAPIView):
    queryset = MobileCharger.objects.all()
    serializer_class = MobileChargerSerializer
class DetailMobileCharger(generics.RetrieveUpdateDestroyAPIView):
    queryset = MobileCharger.objects.all()
    serializer_class = MobileChargerSerializer

class ListHeadphone(generics.ListCreateAPIView):
    queryset = Headphone.objects.all()
    serializer_class = HeadphoneSerializer

class DetailHeadphone(generics.RetrieveUpdateDestroyAPIView):
    queryset = Headphone.objects.all()
    serializer_class = Headphone