from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
