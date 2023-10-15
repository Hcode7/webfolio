from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ProjectForm

# Create your views here.


def home(request):
    project = Project.objects.all()
    context = {'project' : project}
    return render(request, 'pages/index.html', context)


def project_details(request, pk):
    item = Project.objects.get(pk=pk)
    context = {'item' : item}
    return render(request, 'pages/project-detail.html',context)