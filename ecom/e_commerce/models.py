from django.db import models

# Create your models here.
class category(modles.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ImageField(upload_to='e_commerce/product')
    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.name

class product_pics(models.Model):
    sub_image = models.ImageField(upload_to='e_commerce/product')
    product = models.ForeignKey(product,on_delete=models.CASCADE,related_name='images')

    def __str__(self):
        return self.product.name
