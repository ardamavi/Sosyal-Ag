from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    text = models.CharField(max_length=140)

    def __str__(self):
        return (self.name + " - " + self.text)
