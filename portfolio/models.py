from django.db import models
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)
    ects = models.IntegerField(default=4)
    lective_year = models.IntegerField(default=2019)
    description = models.CharField(max_length=500, default='Description')

    def __str__(self):
        return f"{self.name} Y{self.year}S{self.semester}"


class Person(models.Model):
    name = models.CharField(max_length=50)
    linkedin_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    trailer_url = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name
