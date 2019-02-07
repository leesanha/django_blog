from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def board(request):
    posts = Post.objects
    return render(request, "os/board.html", {'posts': posts})

def new(request):
    return render(request, "os/new.html")

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()

    return redirect("/os/"+str(post.id))

def detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)

    return render(request,"os/detail.html",{'post': post})