from datetime import datetime
from django.shortcuts import render
from .models import Post, Comment, Tags
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def post_list(request):
    posts =  Post.objects.all()

    post_by_month_arr = []

    for month in range(1,13):
        post_by_month_arr.append({'posts':Post.objects.filter(published_date__month=month, published_date__year=2021), 'month':month})
    
    print('post by month array', post_by_month_arr)


    context = {'posts':posts, 'postsByMonth':post_by_month_arr}   

    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post =Post.objects.get(pk=pk)
    context = { 'post' : post }
    return render(request, 'blog/post_detail.html', context)

def post_list_per_month(request,pk):
    posts = Post.objects.filter(published_date__month=pk, published_date__year=2021)
    context = {'posts':posts}
    return render(request, 'blog/post_list_per_month.html', context)