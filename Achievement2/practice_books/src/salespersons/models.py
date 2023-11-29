from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# defining Class model


class Salesperson(models.Model):
    # username for each salesperson
    # OneToOne means each username connect to only one salesperson
    # CASCADE: username deleted means salesperson deleted
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    # name of salesperson
    name = models.CharField(max_length=120)

    # text field, default no bio
    bio = models.TextField(default="no bio..")

    def __str__(self):
        # f-string allows to format string
        return f"Profile of {self.username}"
