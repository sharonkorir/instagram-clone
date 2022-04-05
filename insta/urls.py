from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('profile/update', views.profile, name='update_profile'),
    path('profile/<str:username>', PostListView.as_view(), name='profile'),
    path('new/post', views.new_post, name ='new_post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
    path('search/', views.search_results, name='search_results'),
]