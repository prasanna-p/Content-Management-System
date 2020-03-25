from django.urls import path
from blog.views import index
from blog.views import post_details
from blog.views import filter_post

urlpatterns = [
    path('stories',index),
    path('<int:id>',filter_post),
    path('post_info/<int:id>',post_details)
]
