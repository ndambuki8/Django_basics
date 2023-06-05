from django.shortcuts import render
from .models import Post
# Create your views here.
# CRUD - Create, Read/Retrieve, Update, Delete, 

#1 - List all of the posts

def post_list_view(request):
    post_objects = Post.objects.all()

    context = {
        'post_objects':post_objects
    }
    return render(request, "posts/index.html", context)