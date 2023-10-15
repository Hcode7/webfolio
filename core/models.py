from django.db import models

# Create your models here.


class Project(models.Model):
    img = models.ImageField()
    mini_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title