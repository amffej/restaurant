from django.contrib import admin

# Register your models here.
from .models import entree, size, category, addon, addonLimits

admin.site.register(entree)
admin.site.register(size)
admin.site.register(category)
admin.site.register(addon)
admin.site.register(addonLimits)

