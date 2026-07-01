from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    from django.db import models

class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField(blank=True)

        def __str__(self):
            return self.name