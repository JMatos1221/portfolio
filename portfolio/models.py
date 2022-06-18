from tokenize import blank_re
from django.db import models
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)
    ects = models.IntegerField(default=4)
    lective_year = models.IntegerField(default=2019)
    description = models.TextField(max_length=500, default='Description')
    link = models.URLField(default='https://www.ulusofona.pt/')

    def __str__(self):
        return f"{self.name} Y{self.year}S{self.semester}"


class Person(models.Model):
    name = models.CharField(max_length=50, default='')
    linkedin_url = models.URLField(max_length=256, default='')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')
    year = models.IntegerField(default=2019)
    trailer_url = models.URLField(max_length=256, default='')
    thumbnail = models.ImageField(upload_to="projects/", blank=True)

    def __str__(self):
        return self.name


class WebTechnology(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')
    link = models.URLField(max_length=256, default='')

    def __str__(self):
        return self.name


class Laboratory(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')
    link = models.URLField(max_length=256, default='')

    def __str__(self):
        return self.name


class New(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')
    link = models.URLField(max_length=256, default='')
    image = models.ImageField(upload_to="news/", blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=50, default='')
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')

    def __str__(self):
        return f"{self.date} | {self.author} | {self.description}"


class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=256, default='')
    image = models.ImageField(upload_to='contacts/', blank=True)

    def __str__(self):
        return self.name


class TFC(models.Model):
    title = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    advisor = models.CharField(max_length=50, default='')
    resume = models.TextField(max_length=500, default='')
    github_link = models.URLField(max_length=256, default='')
    youtube_link = models.URLField(max_length=256, default='')
    report_link = models.URLField(max_length=256, default='')
    image = models.ImageField(upload_to="tfc/", blank=True)

    def __str__(self):
        return f"{self.author} - {self.title}"
