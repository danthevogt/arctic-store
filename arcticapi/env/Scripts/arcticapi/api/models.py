from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    filename =  models.TextField()
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    