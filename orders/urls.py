from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:cat_id>", views.category, name="category_url"),
    path("item/<int:item_id>", views.item, name="item_url"),
    path("register/", views.register, name="register")
]
