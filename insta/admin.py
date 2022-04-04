from django.contrib import admin
from .models import EmailRecepients, UserProfile, Post


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(EmailRecepients)
admin.site.register(Post)