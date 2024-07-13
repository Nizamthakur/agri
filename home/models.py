
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fish', 'Fish Feed'),
        ('cattle', 'Cattle Feed'),
        ('chicken', 'Chicken Feed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class QuoteRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name