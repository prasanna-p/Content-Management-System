from django.contrib import admin
from blog.models import post
from blog.models import Catogary

# Register your models here.
admin.site.register(post)
admin.site.register(Catogary)
