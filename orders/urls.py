from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entree/<int:entree_id>", views.entree, name="entreeurl"),
    path("register/", views.register, name="register")
]
