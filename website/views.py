from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')
def about_view(request):
    return render(request, 'website/about.html')
def contact_view(request):
    return render(request, 'website/contact.html')

def pricing_view(request):
    return render(request, 'website/pricing.html')

def courses_view(request):
    return render(request, 'website/courses.html')
def teacher_view(request):
    return render(request, 'website/teacher.html')


def test_view(request):
    return render(request,'website/test.html')
    