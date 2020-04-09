from django.urls import path
# from blog.views import index
from blog.views import PostList
# from blog.views import post_details
from blog.views import PostDetailView
# from blog.views import filter_post
from blog.views import FilterPostView
# from blog.views import contact_view
from blog.views import ContactView
# from blog.views import post_form_view
from blog.views import PostFormView
# from blog.views import update_post_form
from blog.views import UpdatePost

urlpatterns = [
    path('stories',PostList.as_view()),
    path('<int:id>',FilterPostView.as_view()),
    # path('post_info/<int:pk>',PostDetailView.as_view()),
    path('post_info/<slug:slug>',PostDetailView.as_view(),name="post_detail"),
    path('contact',ContactView.as_view()),
    path('post',PostFormView.as_view()),
    # path('post/<slug:slug>',update_post_form)
    path('post/<slug:slug>',UpdatePost.as_view())
]
