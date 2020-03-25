from django.db import models
from api.fields import JSONField

# Create your models here.
class MyModel(models.Model):
    json = JSONField()

class Category(models.Model):
    title = models.TextField()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    filename =  models.TextField()
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Sale(models.Model):
    name = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zipcode= models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items = JSONField(default=object)
    payment_intent = JSONField(default=dict)

    