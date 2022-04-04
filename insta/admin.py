from django.contrib import admin
from .models import EmailRecepients, UserProfile


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(EmailRecepients)