from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class makerprofile(models.Model):
    maker_id=models.AutoField(primary_key=True)
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    maker_name=models.CharField(max_length=20)
    maker_email=models.CharField(max_length=20)
    maker_address=models.CharField(max_length=50)
    maker_about=models.CharField(max_length=200)
    maker_phone=models.CharField(max_length=11)