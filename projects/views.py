from django.shortcuts import render
from .models import *

# Create your views here.
def index(request,category=None):
    if category:
        projects = Category.objects.get(title=category).project_set.all()
        print projects[0].title
    else:
        projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects':projects})

def detail(request,project):
    project = Project.objects.get(id=project)
    return render(request, 'projects/detail.html', {'project':project})

