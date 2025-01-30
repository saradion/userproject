
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username