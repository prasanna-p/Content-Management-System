from django.contrib import admin
from inventory.models import user
from inventory.models import product
from inventory.models import order

# Register your models here.
admin.site.register(user)
admin.site.register(product)
admin.site.register(order)
