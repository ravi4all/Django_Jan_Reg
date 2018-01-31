from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser

# Create your views here.
def index(req):
    return render(req, 'index.html')

def register(req):
    if req.method == 'POST':
        form = RegisterUser(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/twitter/')

    else:
        form = RegisterUser()
        context = {'form' : form}
        return render(req, 'includes/registration.html', context)

def profile(req):
    user = req.user

    context = {"user" : user}

    return render(req, 'includes/profile.html', context)
