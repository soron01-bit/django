from django.shortcuts import render
from .models import product


def app(request):
    products = product.objects.all()
    return render(request, 'newApp/app.html', {'products': products})

def about(request):
    return render(request, 'newApp/about.html')


def contact(request):
    return render(request, 'newApp/contact.html')
