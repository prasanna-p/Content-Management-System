from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from account.models import User



class Catogary(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
#title
#content
#status

class post(models.Model):
    statuses = [
        ("D","draft"),
        ("p","published")
        ]
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True,unique=True)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=1,choices=statuses)
    image = models.ImageField(upload_to="blog/post",blank=True)
    Catogary= models.ForeignKey(Catogary,on_delete=models.CASCADE,related_name="posts")
    author = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail",kwargs = {"slug":self.slug})


