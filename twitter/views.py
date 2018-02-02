from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser, EditProfile

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

def view_profile(req):
    user = req.user

    context = {"user" : user}

    return render(req, 'includes/profile.html', context)

def edit_profile(req):
    if req.method == 'POST':
        form = EditProfile(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('/twitter/profile')

    else:
        form = EditProfile(instance=req.user)
        context = {'form' : form}
        return render(req, 'includes/edit_profile.html', context)