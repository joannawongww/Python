from django.db import models

# Create your models here.

# defining Customer class


class Customer(models.Model):
    # class attribute: name and notes
    name = models.CharField(max_length=120)
    notes = models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

    # string representation of object
    # can decide parameter want to use to refer to customer
    # use name to refer to customer
    def __str__(self):
        return str(self.name)
