from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Count
from .models import Item, Category, Cart, Addon
from .forms import SignUpForm

@login_required
def index(request):
    context = {
        #"entrees": Category.objects.values('name'),
        "categories": Category.objects.all()
        #"highPrice": Entree.objects.all().aggregate(Max('price')),
        #"lowPrice": Entree.objects.all().aggregate(Min('price'))
    }
    return render(request, "orders/index.html", context)

@login_required
def item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except item.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "item": item,
        "addons": item.addons.all()
    }   
    return render(request, "orders/item.html", context)

@login_required
def category(request, cat_id):
    try:
        category = Item.objects.filter(category=cat_id) #GET ALL ITEMS FROM GIVEN CATEGORY 
    except category.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "category": category
    }   
    return render(request, "orders/category.html", context)

@login_required
def cart(request): 
    if request.method == "POST":
        item_id = int(request.POST.get("item_id"))
        addons_id = request.POST.getlist("addon_id")
        # perform conversion
        addon_total = 0  
        for i in range(0, len(addons_id)): 
            addons_id[i] = int(addons_id[i]) 
            addon_object = Addon.objects.get(pk=addons_id[i])
            addon_total += addon_object.price
        data = Cart(item_id = item_id, user = request.user, addons_total = addon_total)
        data.save()
        data.addons.add(*addons_id)
    try:
        cartObjects = Cart.objects.filter(user=request.user)
    except cartObjects.DoesNotExist:
        raise Http404("Cart does not exist")
    #get order total
    orderTotal = 0
    for cartObject in cartObjects:
        orderTotal += cartObject.item.price
        if not cartObject.item.addon_free:
            orderTotal += cartObject.addons_total
    context = {
        "cartObjects": cartObjects,
        "orderTotal": orderTotal 
    }        
    return render(request, "orders/cart.html", context)

@login_required
def cart_remove(request, item_id):
    Cart.objects.filter(pk = item_id).delete()        
    return redirect(cart)

@login_required
def orders(request):
    context = {
        "category": "none",
    }   
    return render(request, "orders/orders.html", context)

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = SignUpForm()
    return render(request, "registration/register.html", context={"form":form})