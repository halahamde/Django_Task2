from django.db import models

# Create your models here.
class myuser(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    track=models.CharField(max_length=20)