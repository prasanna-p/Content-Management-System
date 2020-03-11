from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class order(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,related_name="users")
    quantity = models.IntegerField()
    product = models.ManyToManyField(product,related_name="products")

    