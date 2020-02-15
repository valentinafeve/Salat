from django.shortcuts import render
from rest_framework import viewsets, status
from .models import BasicInfo, CSVFile
from .serializers import BasicInfoSerializer, CSVFileSerializer
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
class BasicInfoView(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class CSVFileView(viewsets.ModelViewSet):
    queryset = CSVFile.objects.all()
    serializer_class = CSVFileSerializer

def load_csv(request):
    if request.method == 'POST':
        if request.FILES['csv1'] and request.FILES['csv2']:
            try:
                file1 = request.FILES['csv1']
                file1 = request.FILES['csv2']
                retutn Response({status: 1},  status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({ error:str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
