from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def products(req):
    return render(req, 'includes/products.html')

def cart(req):
    return render(req, 'includes/cart.html')