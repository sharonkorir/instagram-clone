from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('new/post', views.new_post, name ='new_post'),
    path('search/', views.search_results, name='search_results'),
]