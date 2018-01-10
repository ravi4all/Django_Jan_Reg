from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def products(req):
    productList = [
        {'id' : 101, 'name' : 'Apple', 'price' : 55000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id' : 102, 'name' : 'Samsung', 'price' : 45000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id' : 103, 'name' : 'Redmi', 'price' : 12000},
        {'id' : 104, 'name' : 'Vivo', 'price' : 25000},
    ]
    return render(req, 'includes/products.html', {'products' : productList})

def cart(req):
    return render(req, 'includes/cart.html')

def contact(req):
    email = 'ravi.py4all@gmail.com'
    return render(req, 'includes/contact.html', {'contact' : email})