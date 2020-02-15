from django.shortcuts import render
from rest_framework import viewsets
from .models import BasicInfo
from .serializers import BasicInfoSerializer

# Create your views here.
class BasicInfoView(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer
