from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(help_text="Max of 250 Characters", max_length=250)
    
    def __str__(self):
        return f"{self.name}"

class Addon(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in $US", max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"

class AddonLimit(models.Model):
    limit = models.PositiveSmallIntegerField(help_text="How many addons, 0 = none")

    def __str__(self):
        return f"{self.limit}"

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(help_text="Max of 250 Characters", max_length=250)
    price = models.DecimalField(help_text="Price in $US", max_digits=6, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    addonLimit = models.ForeignKey(AddonLimit, on_delete=models.CASCADE)
    addons = models.ManyToManyField(Addon, null=True, blank=True)
    addon_free = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.size} {self.name} {self.category} - {self.price}"

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addons = models.ManyToManyField(Addon, null=True, blank=True)
    addons_total = models.DecimalField(help_text="Price in $US", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.item}" 

class Order(models.Model):
    cartItem = models.ManyToManyField(Cart)

    def __str__(self):
        return f"Order ID:{self.pk}"