from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request): 
    return HttpResponse("This is the about page.")
def contact(request):
    return HttpResponse("This is the contact page.")
def services(request):
    return HttpResponse("This is the services page.")