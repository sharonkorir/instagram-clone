
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    '''
    Profile model acts as blueprint for all profile instances
    '''
    bio = models.CharField(max_length =150)
    profile_photo = CloudinaryField('image')
    # name = models.CharField(max_length=30)
    # email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def search_user(cls,search_term):
        users = cls.objects.filter(user__username__icontains=search_term)
        return users


class likes(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return self.count
 
class Post(models.Model):
    '''
    Post model acts as blueprint for all post instances
    '''
    name = models.CharField(max_length =60)
    caption = models.TextField()
    image = CloudinaryField('image')
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(UserProfile, related_name='likes', blank=True)
    #comments = models.ManyToManyField(comments)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_post(self):
        self.save()

    #return url path after creating a post
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date_posted']

class Comments(models.Model):
    content = models.TextField(max_length =150)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-pk']

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_by_post(cls,post_pk):
        comments = cls.objects.filter(post=post_pk)
        return comments

class EmailRecepients(models.Model):
    '''
    EmailRecepients model acts as blueprint for all email recepients on registation
    '''

    name = models.CharField(max_length=30)
    email = models.EmailField()
    