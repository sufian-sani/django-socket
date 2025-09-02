from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("blog_list")
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", {"form": form})