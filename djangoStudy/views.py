from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def board(request):
    posts = Post.objects
    return render(request, "django/board.html", {'posts': posts})

def new(request):
    return render(request, "django/new.html")

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()

    return redirect("/django/"+str(post.id))

def detail(request, post_id):
    post = get_object_or_404(Post,pk = post_id)

    return render(request, "django/detail.html", {'post': post})