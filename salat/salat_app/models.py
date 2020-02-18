from rest_framework import authentication
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    national_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

class Loan(models.Model):
    information = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    due_date = models.DateField()

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
