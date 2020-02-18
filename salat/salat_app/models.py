from rest_framework import authentication
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    national_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

class Salat(models.Model):
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    name = models.TextField(default='void')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    ordered_date = models.DateField()

class CSVFile(models.Model):
    file = models.FileField()

class SalatAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None
        try:
            user = User(username=username)
            # user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
