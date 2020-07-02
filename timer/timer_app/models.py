from django.db import models

# Create your models here.

class Project(models.Model):
    project_name_text = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name_text

class Time(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_text = models.CharField(max_length=255)
    last_modified = models.DateTimeField('last modified')

    def __str__(self):
        return self.time_text

