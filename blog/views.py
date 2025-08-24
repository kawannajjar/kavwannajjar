from django.shortcuts import render


def blog_view(request):
    return render(request, 'blog/blog.html')

def blog_single(request):
    context = {'title': 'sanandaj kinder',
               'context': "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus itaque", 
               'user': 'kawan',
               'user1': 'ali'}
    return render(request, 'blog/blog-single.html',context)
