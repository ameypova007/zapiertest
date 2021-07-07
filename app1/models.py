from django.db import models

# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=50)
    sender = models.CharField(mafrom django.db import models

# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
