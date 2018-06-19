from django.db import models

# Create your models here.

class info(models.Model):
    enter = models.DateTimeField('Enter')
    exitt = models.DateTimeField('Exit')
    today = models.DateField('Today')
    week = models.IntegerField(default=1)
    month = models.IntegerField(default=1)