from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def login(req):
    username = ""

    if 'username' in req.POST:
        username = req.POST['username']

    else:
        username = ""

    return render(req, 'login.html', {"username" : username})