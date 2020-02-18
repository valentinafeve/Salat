from django.shortcuts import render
from rest_framework import viewsets, status
from .models import BasicInfo, CSVFile
from .serializers import BasicInfoSerializer, CSVFileSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class BasicInfoView(APIView):
    def get(self, request):
        return None

class CSVFileView(APIView):
    def post(self, request):
        logger.info("Post received")
        try:
            if request.FILES['csv1'] and request.FILES['csv2']:
                logger.info("Checking both files...")
                file1 = request.FILES['csv1']
                file2 = request.FILES['csv2']
                logger.info("Reading files...")

                for line in file1.readlines():
                    print(line.decode("utf-8"))

                for line in file1.readlines():
                    print(line.decode("utf-8"))

                return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            logger.error("Exception when trying to read file.")
            return Response({ 'message': 'Error when trying to read file.' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
