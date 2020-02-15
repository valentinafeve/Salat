from django.shortcuts import render
from rest_framework import viewsets
from .models import BasicInfo, CSVFile
from .serializers import BasicInfoSerializer, CSVFileSerializer

# Create your views here.
class BasicInfoView(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class CSVFileView(viewsets.ModelViewSet):
    queryset = CSVFile.objects.all()
    serializer_class = CSVFileSerializer
