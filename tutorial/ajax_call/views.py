from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'form.html')

def login(req):
    username = ""

    errors = []

    if 'username' in req.POST:
        username = req.POST['username']

        if not username:
            errors.append("Please fill this field")
        elif len(username) < 10:
            errors.append("Should be greater than 10")

        else:
            return render(req, 'login.html', {'username' : username})


        return render(req, 'form.html', {"errors" : errors})