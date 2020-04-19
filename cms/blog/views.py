from django.shortcuts import render,HttpResponse,get_object_or_404
from blog.models import post
from blog.models import Catogary
from blog.forms import ContactForm
from blog.forms import PostForm
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def index(request,*args,**kwargs):
#     published_post = post.objects.filter(status='p')
#     titels = [post.title for post in published_post]
#     title_str = "\n".join(titels)
#     return HttpResponse(title_str)

# view function
# def index(request,*args,**kwargs):

#      published_post = post.objects.filter(status="p")
#      category = Catogary.objects.all()
#      return render(request,"blog/index.html",context={"posts":published_post,"category":category})

# class PostList(View):

#     def get(self,request,*args,**kwargs):

#         published_post = post.objects.filter(status="p")
#         category = Catogary.objects.all()
#         return render(request,"blog/index.html",context={"posts":published_post,"category":category})


class PostList(ListView):
    
    model = post
    queryset = post.objects.filter(status = "p")
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Catogary.objects.all()
        return context


# def post_details(request,id,*args,**kwargs):

#     try:
#         post_content = post.objects.get(id=id)
#         return render(request,"blog/post_details.html",context={"post":post_content})
#     except:
#         return HttpResponse("invalid id")

# class PostDetailView(View):

#     def get(self,request,id,*args,**kwargs):

#         try:

#             post_content = post.objects.get(id=id)
#             return render(request,"blog/post_details.html",context={"post":post_content})

#         except:

#             return HttpResponse("invalid id")


class PostDetailView(LoginRequiredMixin,DetailView):

    login_url = 'login'
    model = post
    template_name = "blog/post_details.html"
    context_object_name = "post"


# def filter_post(request,id,*args,**kwargs):

#     cat =  Catogary.objects.get(id=id)
#     posts = cat.posts.all()
#     category = Catogary.objects.all()
#     return render(request,"blog/index.html",context={"posts":posts,"category":category})

# class FilterPostView(View):

#     def get(self,request,id,*args,**kwargs):

#         cat =  Catogary.objects.get(id=id)
#         posts = cat.posts.filter(status = "p")
#         category = Catogary.objects.all()
#         return render(request,"blog/index.html",context={"posts":posts,"category":category})

class FilterPostView(ListView):

    model = Catogary
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        context["category"] = Catogary.objects.all()
        return context

    def get_queryset(self):
        cat = get_object_or_404(Catogary,id = self.kwargs['id'])
        return cat.posts.filter(status = "p")

# def contact_view(request,*args,**kwargs):
    
#     if request.method == "GET":
#         form = ContactForm()
#         return render(request,"blog/contact.html",context={"form":form})
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print("hi")
#             print(form.cleaned_data)
#             return HttpResponse("thank you")
#         else:
#             return render(request,"blog/contact.html",context={"form":form})


# class ContactView(View):

#     def get(self,request,*args,**kwargs):

#         form = ContactForm()
#         return render(request,"blog/contact.html",context={"form":form})

#     def post(self,request,*args,**kwargs):

#         form = ContactForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("thank you")
#         else:
#             return render(request,"blog/contact.html",context={"form":form})

class ContactView(FormView):
    
    form_class = ContactForm
    template_name = "blog/contact.html"
    success_url = "contact"


# def post_form_view(request,*args,**kwargs):

#     if request.method == "GET":
#         form = PostForm()
#         return render(request,"blog/post.html",context={"form":form})
    
#     else:
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("thank you")
#         else:
#             return render(request,"blog/post.html",context={"form":form})

# class PostFormView(View):

#     def get(self,request,*args,**kwargs):

#         form = PostForm()
#         return render(request,"blog/post.html",context={"form":form})
    
#     def post(self,request,*args,**kwargs):

#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("thank you")
#         else:
#             return render(request,"blog/post.html",context={"form":form})

class PostFormView(CreateView):

    # model = post
    # fields = ['title','content','status','image','Catogary','author']
    template_name = "blog/post.html"
    # success_url = reverse("post_detail",kwargs = {"slug":self.slug})
    form_class = PostForm



# def update_post_form(request,id,*args,**kwargs):
#     try:
#         post_info = post.objects.get(id = id)
#     except:
#         return HttpResponse("invalid id")

#     if request.method == "GET":
#         form = PostForm(instance=post_info)
#         return render(request,"blog/post.html",context={"form":form})
    
#     else:
#         form = PostForm(request.POST,request.FILES,instance=post_info)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("thank you")
#         else:
#             return render(request,"blog/post.html",context={"form":form})

class UpdatePost(UpdateView):
    model = post
    form_class = PostForm
    template_name = "blog/post.html"
    