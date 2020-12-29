from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list": qs
    }
    
    return render(request, "blog/post_list.html", context)


def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:list")
    context= {
        "form":form
    }
    
    return render(request, "blog/post_create.html", context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method=="POST":
        post.delete()
        return redirect("blog:list")
    
    context = {
        "post":post
    }
    
    return render(request, "blog/post_delete.html", context)

def post_update(request, id):
    object = get_object_or_404(Post, id = id)
    form = PostForm(instance=object)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=object)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:list")
        
    context = {
        "object":object,
        "form":form
    }
        
    return render(request, "blog/post_update.html", context)

