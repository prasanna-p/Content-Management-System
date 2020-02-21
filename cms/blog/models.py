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

class post(models.Model):
    statuses = [
        ("D","draft"),
        ("p","published")
        ]
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses)
    Catogary= models.ForeignKey(Catogary,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
