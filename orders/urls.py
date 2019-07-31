from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:cat_id>", views.category, name="category_url"),
    path("item/<int:item_id>", views.item, name="item_url"),
    path("register/", views.register, name="register"),
    path("orders/", views.orders, name="orders"),
    path("orders_admin/", views.orders_admin, name="orders_admin"),
    path("cart/", views.cart, name="cart"),
    path("cart_rm/<int:item_id>", views.cart_remove, name="cart_remove"),
    path("order_cp/<int:order_id>", views.order_complete, name="order_complete"),
    path("checkout/", views.checkout, name="checkout"),
    #path("cart_rm/<int:cart_item_id>", views.cart_remove, name='cart_remove'),
    
]
