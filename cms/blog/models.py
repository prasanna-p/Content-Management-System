from django.db import models



class Catogary(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
#title
#content
#status
class author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class post(models.Model):
    statuses = [
        ("D","draft"),
        ("p","published")
        ]
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=1,choices=statuses)
    image = models.ImageField(upload_to="blog/post",blank=True)
    Catogary= models.ForeignKey(Catogary,on_delete=models.CASCADE,related_name="posts")
    author = models.ForeignKey(author,on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return self.title
