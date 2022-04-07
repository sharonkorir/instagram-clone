from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index,name = 'index'),
    path('profile/update', views.profile, name='update_profile'),
    #path('profile/<str:username>', PostListView.as_view(), name='profile'),
    path('profile/<str:username>', views.profile_posts, name='profile'),
    path('user-profile/<str:username>', views.user_profile, name='user_profile'),
    path('new/post', PostCreateView.as_view(), name ='post_create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
    path('post/<int:pk>/update_caption/',PostUpdateView.as_view(),name = 'post_update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post_delete'),
    path('search/', views.search_results, name='search_results'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name ='comment_create'),
]