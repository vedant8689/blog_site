from django.db import models
from django.urls import reverse
from django.utils import timezone
#django has already created user model
from django.contrib.auth.models import User

#for creating database and tables
#post table --> inherited from models.model
class Post(models.Model):
    #attribute will be field
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #new entry -> update time

    #dunder STR method to make more descriptive
    def __str__(self):
       return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
#user table





