from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
    objects = models.Manager()
    
    project_name_text = models.CharField(max_length=255)
    time_text = models.CharField(max_length=255, default="0:0:0")

    current_time = datetime.now()
    last_modified = models.DateTimeField('last modified', default=current_time)

    def __str__(self):
        return self.project_name_text

