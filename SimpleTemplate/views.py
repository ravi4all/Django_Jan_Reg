from django.shortcuts import render
from datetime import datetime

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def index(request):
    now = datetime.now().date()
    time = datetime.now().time()
    return render(request, 'index.html', {"today":now, "time":time})

def contact(request):
    phNo = '989898989'
    return render(request, 'contact.html', {"contact": phNo})