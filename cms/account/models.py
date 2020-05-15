from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500,blank=True,default="I love to write blogs......")
    image = models.ImageField(default='default.jpg',upload_to="proflie/",blank=True)
    is_author = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]

    def get_absolute_url(self):
        return reverse("profile",kwargs = {'pk':self.pk})

    def save(self,*args,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


