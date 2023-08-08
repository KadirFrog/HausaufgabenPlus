from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomRegistrationForm, CustomAuthenticationForm, PostForm
from haplus.models import Post
from .forms import CustomRegistrationForm
from .models import CustomUser

@login_required
def profile(request):
    return render(request, "profile.html")

@login_required
def main(request):
    user = request.user
    posts = Post.objects.filter(klasse=user.school_class)
    return render(request, 'main.html', {'posts': posts, 'user': user})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # Handle successful form submission
            return redirect('home')  # Redirect to the home page
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("login")

def custom_404(request, exception):
    return render(request, 'login.html', status=404)