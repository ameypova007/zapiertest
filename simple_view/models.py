from django.db import models



class Message1(models.Model):
    message = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    receiver = modfrom django.db import models



class Message1(models.Model):
    message = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
