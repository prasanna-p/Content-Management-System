from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm 
from account.forms import SignUpForm
from account.forms import ProfileForm
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
class UserCreation(CreateView):

    form_class = SignUpForm
    template_name = "account/signup.html"
    success_url = '/stories'


class ProfileView(LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin,DetailView,UpdateView):

    login_url = 'login'
    model = User
    form_class = ProfileForm
    template_name = "account/profile.html"
    context_object_name = "user"
    permission_required = 'account.change_User'
    # success_url = 'profile'

    def test_func(self,*args,**kwargs):
        # print(self.kwargs.get('pk'))
        # print(self.request.user.pk)
        if self.request.user.pk == self.kwargs.get('pk'):

            return True

        else:

            return False

# class ProfileUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    
#      model = User
#      form_class = ProfileForm
#      template_name = 'account/profile'
#      login_url = 'login'
#      permission_required = 'account.change_User'
#      success_url = 'profile'





# class UpdatePost(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,UpdateView):
#     model = post
#     form_class = PostForm
#     template_name = "blog/post.html"
#     login_url = 'login'
#     permission_required = 'blog.change_post'

#     def test_func(self,*args,**kwargs):
#         slug = self.kwargs.get('slug')
#         post_info = post.objects.get(slug=slug)
#         if self.request.user.get_username() == post_info.author.get_username():
#             return True
#         else:
#             return False

    
        
        