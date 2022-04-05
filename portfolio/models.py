from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Job(models.Model):
    # voice_path=models.FileField(upload_to='media/audio/')
    company = models.CharField(max_length=250,blank=True,null=False)
    description = models.CharField(max_length=250,blank=True,null=False)
