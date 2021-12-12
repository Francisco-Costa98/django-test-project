from django.shortcuts import render
from .models import Post, Comment, Tags
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts =  Post.objects.all()
    comments = Comment.objects.all()
    tags = Tags.objects.all()
    context = {'posts':posts, 'tags':tags, 'comments': comments}   
    print(context)

    return render(request, 'blog/post_list.html', context)