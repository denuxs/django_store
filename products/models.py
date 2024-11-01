from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to="products/", default="default.jpg", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
