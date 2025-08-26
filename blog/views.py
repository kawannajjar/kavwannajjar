from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('-created_date')
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    # می‌تونی تگ‌ها یا مطالب مرتبط هم اضافه کنی
    return render(request, 'blog/blog-single.html', context)
