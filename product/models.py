from django.db import models

#1-Homework
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=15)
    descriptions = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=25)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
