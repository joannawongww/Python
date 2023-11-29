from django.db import models

# Create your models here.

# define user class


class User(models.Model):
    # username, max length 20 char
    username = models.CharField(max_length=20)
    # password, max length 20 char
    password = models.CharField(max_length=20)

    # string representation by username
    def __str__(self):
        return str(self.username)
