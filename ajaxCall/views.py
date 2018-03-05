from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(req):
    return render(req, 'index.html')

def login(req):

    errors = []

    if 'username' in req.POST:
        username = req.POST['username']

        if not username:
            errors.append("This field is required")
        else:
            return render(req, 'login.html', {'username' : username})

        return render(req, 'index.html', {'errors':errors})

def loginValidate(req):
    errors = []
    if 'username' in req.GET:
        username = req.GET['username']

        if username == "":
            errors.append("This field is required")
        elif len(username) < 10:
            errors.append("Must be greater than 10")

        return JsonResponse(errors, safe=False)
