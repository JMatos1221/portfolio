
from django.urls import path
from . import views

app_name = 'pw'

urlpatterns = [
    path('', views.home_view),
    path('home', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('projects', views.projects_view, name='projects'),
    path('web-programming', views.web_programming_view, name='web-programming'),
    path('blog', views.blog_view, name='blog'),
    path('about-website', views.about_website_view, name='about-website'),
    path('contact', views.contact_view, name='contact'),
]
