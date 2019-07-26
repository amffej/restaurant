from django.contrib import admin

# Register your models here.
from .models import Entree, Size, Category, Addons, AddonLimits

admin.site.register(Entree)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Addons)
admin.site.register(AddonLimits)

