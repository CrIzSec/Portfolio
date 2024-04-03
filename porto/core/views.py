from django.shortcuts import render, get_object_or_404
from .models import Project, Image

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project(request):
    post = Project.objects.all()
    return render(request, 'project.html', {
        'post': post,
    })

def detail_view(request, id):
    posts = Project.objects.all()
    post = get_object_or_404(posts, id=id)
    photos = Image.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post': post,
        'photos':photos,
    })