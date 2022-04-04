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
    post_date = models.DateTimeField(auto_now_add=True)
    