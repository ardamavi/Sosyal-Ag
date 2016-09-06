from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=112)

    def __str__(self):
        return (self.name + " - " + self.text)
