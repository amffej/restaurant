from django.db import models

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Addons(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in $US", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class AddonLimits(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Entree(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in $US", max_digits=6, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    addonLimits = models.ForeignKey(AddonLimits, on_delete=models.CASCADE)
    addons = models.ManyToManyField(Addons)
    addon_free = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.size} {self.name} {self.category} - {self.price}"