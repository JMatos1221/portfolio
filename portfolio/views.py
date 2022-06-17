from django.shortcuts import render
from portfolio.forms import PostForm, TFCForm
from .models import TFC, Contact, Laboratory, New, Post, Project, Subject, WebTechnology


def home_view(request):
    return render(request, 'portfolio/home.html')


def about_view(request):
    subjects = Subject.objects.all()

    subjects = sorted(subjects, key=lambda x: (x.year, x.semester, x.name))

    return render(request, 'portfolio/about.html', {'subjects': subjects})


def projects_view(request):
    if request.method == 'POST':
        form = TFCForm(request.POST or None, request.FILES)

        duplicate = False

        if form.is_valid():
            for tfc in TFC.objects.all():
                if tfc.title == form.instance.title:
                    duplicate = True

            if not duplicate:
                form.save()

    form = TFCForm()

    projects = Project.objects.all()
    tfc = TFC.objects.all()

    projects = sorted(projects, key=lambda p: (p.year, p.name))
    tfc = sorted(tfc, key=lambda t: (t.title, t.author))

    context = {
        'projects': projects,
        'tfc': tfc,
        'form': form
    }

    return render(request, 'portfolio/projects.html', context)


def web_programming_view(request):
    technologies = WebTechnology.objects.all()
    laboratories = Laboratory.objects.all()
    news = New.objects.all()

    technologies = sorted(technologies, key=lambda t: t.name)
    laboratories = sorted(laboratories, key=lambda t: t.name)
    news = sorted(news, key=lambda n: n.name)

    context = {
        'technologies': technologies,
        'laboratories': laboratories,
        'news': news
    }

    return render(request, 'portfolio/web-programming.html', context)


def blog_view(request):
    if request.method == 'POST':
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
