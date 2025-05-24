from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATAGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Software', 'Software'),
    ('Stationary', 'Stationary'),
    ('Health', 'Health'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    #price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATAGORY_CHOICES , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-----{self.quantity}'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, null=False)
    order_quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product.name} ordered by {self.user.username} on {self.order_date}'