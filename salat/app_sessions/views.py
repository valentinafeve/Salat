from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response

def login(request):
    print(request.POST['username'])
    print(request.POST['password'])
    return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
