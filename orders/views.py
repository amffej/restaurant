from django.http import HttpResponse
from django.shortcuts import render
from .models import Entree

# Create your views here.
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
    print("hello")
    return render(request, "orders/index.html", context)
    #return HttpResponse("Project 3: TODO")

