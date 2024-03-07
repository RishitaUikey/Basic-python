from django.http import HttpResponse
from django.shortcuts import render

# view for home
def home(request):
    return render(request,"home.html")