from django.contrib import admin

# Register your models here.
from .models import Profile

#register model
admin.site.register(Profile)
