from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class userprofile(models.Model):
    user_id=models.AutoField(primary_key=True)
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    user_location=models.CharField(max_length=50)
    user_address=models.CharField(max_length=200)
    user_mobile=models.CharField(max_length=11)