from django.shortcuts import render,HttpResponse
from blog.models import post
from blog.models import Catogary

# Create your views here.
# def index(request,*args,**kwargs):
#     published_post = post.objects.filter(status='p')
#     titels = [post.title for post in published_post]
#     title_str = "\n".join(titels)
#     return HttpResponse(title_str)
def index(request,*args,**kwargs):
     published_post = post.objects.filter(status="p")
     category = Catogary.objects.all()
     return render(request,"blog/index.html",context={"posts":published_post,"category":category})



def post_details(request,id,*args,**kwargs):
    try:
        post_content = post.objects.get(id=id)
        return render(request,"blog/post_details.html",context={"post":post_content})
    except:
        return HttpResponse("invalid id")

def filter_post(request,id,*args,**kwargs):
    cat =  Catogary.objects.get(id=id)
    posts = cat.posts.all()
    category = Catogary.objects.all()
    return render(request,"blog/index.html",context={"posts":posts,"category":category})