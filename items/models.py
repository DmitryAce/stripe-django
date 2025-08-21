from django.db import models

class Item(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'USD'),
        ('eur', 'EUR'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd')
    
    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def calculate_total(self):
        total = sum(item.price for item in self.items.all())
        self.total_price = total
        self.save()
        return total

class Discount(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='discount')
    percent_off = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_coupon_id = models.CharField(max_length=50, blank=True, null=True)

class Tax(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='tax')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_tax_id = models.CharField(max_length=50, blank=True, null=True)