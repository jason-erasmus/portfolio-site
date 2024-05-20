from django.shortcuts import get_object_or_404, render

from .models import Project, Tag


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
