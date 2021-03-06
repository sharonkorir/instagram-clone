from email import message
from .models import EmailRecepients, Post, User, UserProfile, Comments
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
@login_required(login_url='login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts,})

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
            #fetch user posts
            posts = Post.objects.filter(profile=request.user)
            #succesful update message
            messages.success(request, f'Your account has been updated')
            # return redirect('profile')
            return render(request,'users/profile.html', {'posts':posts})
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)

    context = {
      'p_form': p_form,
      'posts': Post.objects.filter(profile = request.user)
    }

    return render(request, 'users/update_profile.html', context)

def profile_posts(request, username):
  posts = Post.objects.filter(profile=request.user)
  user = UserProfile.objects.filter(user=request.user)
  return render(request, 'users/profile.html', {'posts':posts, 'user':user})

def user_profile(request, username):
  posts = Post.objects.filter(profile__userprofile__user__username=username)
  user = UserProfile.objects.filter(user__username=username)
  return render(request, 'users/profile.html', {'posts':posts, 'user':user})

def get_comments(request,pk):

    comments = Comments.get_comments_by_post(pk)
    return render(request, 'index.html', {'comments':comments})

#class view for individual posts that inherits from DetailView
class PostDetailView(DetailView):
    model = Post

#class view for creating posts that inherits from CreateView
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['name', 'image', 'caption']
    
    def form_valid(self,form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

#class view for updating post caption that inherits from UpdateView
class PostUpdateView(LoginRequiredMixin,
UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['caption']
    
    def form_valid(self,form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

    #confirm only post owner can update caption
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.profile:
            return True
        return False

#class view for deleting posts that inherits from DeleteView
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    #confirm only post owner can delete
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.profile:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['content']
    success_url = '/'

    def form_valid(self,form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

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


