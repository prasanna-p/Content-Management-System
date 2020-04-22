from django.contrib import admin
from blog.models import post
from blog.models import Catogary
# from blog.models import author

# Register your models here.
admin.site.register(post)
admin.site.register(Catogary)
# admin.site.register(author)
