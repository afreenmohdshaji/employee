from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name=models.CharField(max_length=40,unique=True)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=40)
    specs=models.CharField(max_length=200)
    display=models.CharField(max_length=200)

    def __str__(self):
        return self.name