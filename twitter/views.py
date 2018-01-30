from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(req):
    return render(req, 'index.html')

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)

        if form.is_valid():
            form.save()
            return render(req, '/twitter/')

    else:
        form = UserCreationForm()
        context = {'form' : form}
        return render(req, 'includes/registration.html', context)
