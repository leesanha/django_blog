from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
import json
from .models import Post

# Create your views here.
def board(request):
    posts = Post.objects
    return render(request, "algorithm/board.html", {'posts': posts})

def new(request):
    return render(request, "algorithm/new.html")

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.pub_date = timezone.datetime.now()
    post.body = request.GET['body']
    post.save()

    return redirect("/algorithm/"+str(post.id))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request,"algorithm/detail.html",{'post':post})

def more(request):
    id = request.POST.get('pk',None)
    post = get_object_or_404(Post, pk = id)

    ret = {
        'body': post.body
    }

    return HttpResponse(json.dumps(ret), content_type="application/json")