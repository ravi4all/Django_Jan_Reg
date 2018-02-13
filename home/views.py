from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomeForm
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-datetime')
        current_user = request.user
        # friends = User.objects.all()
        friends = User.objects.exclude(id=request.user.id)
        args = {
            'form' : form,
            'posts' : posts,
            'current_user' : current_user,
            'friends' : friends
        }

        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()

        args = {'form':form, 'text':text}

        return render(request, self.template_name, args)

