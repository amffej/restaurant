from django.contrib import admin

# Register your models here.
from .models import Item, Size, Category, Addon, AddonLimit, Cart, Order, OrderStatus

class itemAdmin(admin.ModelAdmin):
    filter_horizontal = ("addons",)

admin.site.register(Item, itemAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Addon)
admin.site.register(AddonLimit)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderStatus)

