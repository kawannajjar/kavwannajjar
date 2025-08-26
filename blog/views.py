from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    context = {'post': post}
    # می‌تونی تگ‌ها یا مطالب مرتبط هم اضافه کنی
    return render(request, 'blog/blog-single.html', context)
