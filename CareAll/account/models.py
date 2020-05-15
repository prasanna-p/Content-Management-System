from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):

    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500,blank=True,default="I love to write blogs......")
    image = models.ImageField(default='default.jpg',upload_to="proflie/",blank=True)

    def save(self,*args,**kwargs):

        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# Create your models here.
