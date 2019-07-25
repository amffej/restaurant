from django.db import models

# Create your models here.
class size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class addon(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class addonLimits(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class entree(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in $US", max_digits=4, decimal_places=2)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    addonLimits = models.ForeignKey(addonLimits, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.size} {self.name} {self.category} - {self.price}"