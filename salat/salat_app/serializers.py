from rest_framework import serializers
from .models import BasicInfo, CSVFile

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = ('id','name','score')

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        read_only = True
        required = False
        model = CSVFile
        fields = ('file',)
