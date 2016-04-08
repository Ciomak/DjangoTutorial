from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_lenght=200)
    pubDate = models.DateTimeField('pub_date')