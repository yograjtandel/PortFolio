from os import name
from django.db import models
from django.db.models import fields

# Create your models here.

class Resume(models.Model):
    resume_file = models.FileField(upload_to ='static/uploads/')

class skills(models.Model):
    name = fields.CharField(max_length=200)