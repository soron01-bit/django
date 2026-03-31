from django.shortcuts import render
from newApp.models import product

def home(request):
    products = product.objects.filter(status='available').order_by('-created_at')
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

def services(request):
    return render(request, 'newApp/app.html')