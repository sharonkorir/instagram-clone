from .models import EmailRecepients, Post, User, UserProfile
from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm, NewPostForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def register(request):
    '''
    Register a new user on registration and create user profile using signals
    '''
    if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        #username = form.cleaned_data.get('username')
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        #welcome email
        recipient = EmailRecepients(name = username,email =email)
        recipient.save()
        send_welcome_email(username,email)
        #succesful log in message
        messages.success(request, f'Your  Insta-clone account had been created successfully')
        
        return redirect('login')
    else:
      form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
    
@login_required(login_url='login/')
def profile(request):
    '''
    returns user profile if user is authenticated
    '''
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if p_form.is_valid():
            p_form.save()
            #succesful update message
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)

    context = {
      'p_form': p_form,
      'posts': Post.objects.filter(profile = request.user)
    }

    return render(request, 'users/profile.html', context)

@login_required(login_url='login/')
def new_post(request):
    '''
    Creates and saves a user post.
    '''
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def search_results(request):
    '''
    Function to search for users
    
    Args: username
    '''

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = UserProfile.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})