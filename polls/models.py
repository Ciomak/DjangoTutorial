from __future__ import unicode_literals

from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_lenght=200)
    pubDate = models.DateTimeField('pub_date')
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(mac_lenght=200)
    vote = models.IntegerField()