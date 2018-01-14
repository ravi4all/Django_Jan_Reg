from django.shortcuts import render

productList = []
productList.extend([
        {'id' : 101, 'name' : 'Apple', 'price' : 55000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id' : 102, 'name' : 'Samsung', 'price' : 45000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id' : 103, 'name' : 'Redmi', 'price' : 12000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id' : 104, 'name' : 'Vivo', 'price' : 25000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 107, 'name': 'Redmi', 'price': 13000,
         'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 106, 'name': 'Samsung', 'price': 35000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 105, 'name': 'Apple', 'price': 65000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 108, 'name': 'Vivo', 'price': 20000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 109, 'name': 'Apple', 'price': 75000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 110, 'name': 'Samsung', 'price': 25000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 111, 'name': 'Redmi', 'price': 10000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 112, 'name': 'Vivo', 'price': 18000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
    ])

# Create your views here.
def index(req):
    return render(req, 'index.html')

def products(req):
    return render(req, 'includes/products.html', {'products' : productList})

def cart(req):
    return render(req, 'includes/cart.html')

def contact(req):
    email = 'ravi.py4all@gmail.com'
    return render(req, 'includes/contact.html', {'contact' : email})

def sortByPrice(req):
    sortedByPrice = sorted(productList, key=lambda x : x['price'])

    return render(req, 'includes/products.html', {'products' : sortedByPrice})

def searchProduct(req):
    if 'productName' in req.GET:
        productName = req.GET['productName']

    searchResult = list(filter(lambda x: x['name'] == productName, productList))
    # print("Searching for",productName)
    # print("Searching in",productList)
    # print(searchResult)
    return render(req, 'includes/products.html', {"products":searchResult})