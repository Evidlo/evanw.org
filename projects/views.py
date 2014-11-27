from django.shortcuts import render
from .models import *

# Create your views here.
def project_index(request):
	projects = Project.objects.all()
	return render(request, 'projects/index.html', {'projects':projects})

