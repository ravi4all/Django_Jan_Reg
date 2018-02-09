from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser, EditProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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

@login_required
def view_profile(req):
    user = req.user

    context = {"user" : user}

    return render(req, 'includes/profile.html', context)

@login_required
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

@login_required
def change_password(req):
    if req.method == 'POST':
        form = PasswordChangeForm(data=req.POST, user=req.user)
        if form.is_valid():
            form.save()
            return redirect('/twitter/profile')
    else:
        form = PasswordChangeForm(user=req.user)
        context = {'form' : form}
        return render(req, 'includes/change_password.html', context)