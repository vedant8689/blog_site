from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

# one profile one account  --> one to one relationship
class Profile(models.Model):
    #one to one relationshio between profile and user
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    # use of dunder str
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # resizing image
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # im=request.user.profile.image
        img=Image.open(self.image.path)
        if img.height >= 300 and img.width >= 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img().save(self.image.path)
