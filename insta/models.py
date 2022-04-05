
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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

class likes(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return self.count

class comments(models.Model):
    content = models.CharField(max_length =150)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Post(models.Model):
    '''
    Post model acts as blueprint for all post instances
    '''
    name = models.CharField(max_length =60)
    caption = models.TextField()
    image = CloudinaryField('image')
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(likes)
    comments = models.ManyToManyField(comments)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class EmailRecepients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    