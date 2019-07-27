from django.contrib import admin

# Register your models here.
from .models import Entree, Size, Category, Addons, AddonLimits

class entreeAdmin(admin.ModelAdmin):
    filter_horizontal = ("addons",)

admin.site.register(Entree, entreeAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Addons)
admin.site.register(AddonLimits)

