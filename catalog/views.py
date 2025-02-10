from django.http import HttpResponse
from django.template import loader
from catalog.models import Location



from django.shortcuts import render

def show_map(request):
    return render(request, "index.html")
