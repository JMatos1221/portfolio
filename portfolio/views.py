from django.shortcuts import render
from .models import Contact, Project, Subject, Person, WebTechnology
import datetime


def home_view(request):
    return render(request, 'portfolio/home.html')


def about_view(request):
    subjects = Subject.objects.all()

    subjects = sorted(subjects, key=lambda x: (x.year, x.semester, x.name))

    return render(request, 'portfolio/about.html', {'subjects': subjects})


def projects_view(request):
    projects = Project.objects.all()

    projects = sorted(projects, key=lambda p: (p.year, p.name))

    return render(request, 'portfolio/projects.html', {'projects': projects})


def web_programming_view(request):
    technologies = WebTechnology.objects.all()

    technologies = sorted(technologies, key=lambda t: t.name)

    return render(request, 'portfolio/web-programming.html', {'technologies': technologies})


def blog_view(request):
    return render(request, 'portfolio/blog.html')


def about_website_view(request):
    return render(request, 'portfolio/about-website.html')


def contact_view(request):
    contacts = Contact.objects.all()

    contacts = sorted(contacts, key=lambda c: c.name)

    return render(request, 'portfolio/contact.html', {'contacts': contacts})
