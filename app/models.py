from django.db import models

# Create your models here.

class chat(models.Model):
    content = models.CharField(max_length=255)
    group = models.CharField(max_length=50)
    person = models.CharField(max_length=200)
    timestamp =models.DateTimeField(auto_now=True)

class group(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name