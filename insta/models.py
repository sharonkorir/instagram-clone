from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    '''
    Post model acts as blueprint for all post instances
    '''
    name = models.CharField(max_length =60)
    caption = models.TextField()
    image = CloudinaryField('image')
    #profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    #likes = models.ManyToMannyField(likes, on_delete = models.DO_NOTHING)
    #comments = models.ManyToManyField(comments, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    
class likes(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return self.count

class comments(models.Model):
    content = models.CharField(max_length =150)
    #profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Profile(models.Model):
    '''
    Profile model acts as blueprint for all profile instances
    '''
    bio = models.CharField(max_length =150)
    profile_photo = CloudinaryField('image')
    