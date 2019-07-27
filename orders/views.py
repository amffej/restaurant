from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Entree

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
def index(request):
    context = {
        "entrees": Entree.objects.all()
    }
    return render(request, "orders/index.html", context)

def entree(request, entree_id):
    try:
        entree = Entree.objects.get(pk=entree_id)
    except Entree.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entree": entree,
        "addons": entree.addons.all()
    }
    return render(request, "orders/entree.html", context)