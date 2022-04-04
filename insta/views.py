from .models import EmailRecepients, UserProfile
from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')

def register(request):
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
    return render(request, 'users/profile.html')