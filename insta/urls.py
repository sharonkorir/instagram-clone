from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListViewIndex

urlpatterns=[
    path('',PostListViewIndex.as_view(),name = 'index'),
    path('register/', views.register, name='register'),
    path('profile/update', views.profile, name='update_profile'),
    #path('profile/<str:username>', PostListView.as_view(), name='profile'),
    path('profile/<str:username>', views.profile_posts, name='profile'),
    #path('new/post', views.new_post, name ='new_post'),
    path('new/post', PostCreateView.as_view(), name ='post_create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
    path('post/<int:pk>/update_caption/',PostUpdateView.as_view(),name = 'post_update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post_delete'),
    path('search/', views.search_results, name='search_results'),
]