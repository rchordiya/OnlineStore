from django.shortcuts import render
from . models import Store


def store(request):
    store_details = Store.objects.all()
    return render(request, 'index.html', {'store_details': store_details})

def location(request):
    return render(request, 'location.html', {})