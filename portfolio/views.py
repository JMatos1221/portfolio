from django.shortcuts import render

from portfolio.forms import PostForm
from .models import Contact, Laboratory, New, Post, Project, Subject, WebTechnology


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

    laboratories = Laboratory.objects.all()

    laboratories = sorted(laboratories, key=lambda t: t.name)

    news = New.objects.all()

    news = sorted(news, key=lambda n: n.name)

    context = {
        'technologies': technologies,
        'laboratories': laboratories,
        'news': news
    }

    return render(request, 'portfolio/web-programming.html', context)


def blog_view(request):
    form = PostForm(request.POST or None)

    duplicate = False

    if form.is_valid():
        for post in Post.objects.all():
            if post.description == form.instance.description:
                duplicate = True

        if not duplicate:
            form.save()

    form = PostForm()

    posts = Post.objects.all()

    posts = sorted(posts, key=lambda p: p.date, reverse=True)

    context = {
        'form': form,
        'posts': posts
    }

    return render(request, 'portfolio/blog.html', context)


def contact_view(request):
    contacts = Contact.objects.all()

    contacts = sorted(contacts, key=lambda c: c.name)

    return render(request, 'portfolio/contact.html', {'contacts': contacts})
