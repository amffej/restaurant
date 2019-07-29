from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Count
from .models import Entree, Category
from .forms import SignUpForm 

# Create your views here.
'''
def index(request):
    entrees = Entree.objects.get(pk=5)
    yooo = entrees.addons.all()
    x = []
    for item in yooo:
        x.append(item.name)
    #context = {
     #   "Entrees": entrees.name,
        #"Addons": addons
    #}
    #print("hello")
    #return render(request, "orders/index.html", context)
    return HttpResponse("Project 3: TODO")
'''
# Create your views here.
@login_required
def index(request):
    context = {
        #"entrees": Category.objects.values('name'),
        "entrees": Category.objects.all()
        #"highPrice": Entree.objects.all().aggregate(Max('price')),
        #"lowPrice": Entree.objects.all().aggregate(Min('price'))
    }
    return render(request, "orders/index.html", context)

def item(request, item_id):
    try:
        item = Entree.objects.get(pk=item_id)
    except item.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "item": item,
        "addons": item.addons.all()
    }   
    return render(request, "orders/item.html", context)

def category(request, cat_id):
    try:
        category = Entree.objects.filter(category=cat_id) #GET ALL ITEMS FROM GIVEN CATEGORY #TODO NEED TO CHANGE MODEL FOR ENTREE TO ITEM
    except category.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "category": category
    }   
    return render(request, "orders/category.html", context)

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