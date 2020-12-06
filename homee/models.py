from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class roleassign(models.Model):
    roleid=models.AutoField(primary_key=True)
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=15)
