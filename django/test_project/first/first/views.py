from django.http import HttpResponse
from django.shortcuts import render

# view for home
def home(request):
    return render(request,"home.html")

def ptwo(request):
    return HttpResponse("Welcome to Page 2")

def pthree(request):
    return HttpResponse("Welcome to Page 3")

def pfour(request):
    return HttpResponse("Welcome to Page 4")