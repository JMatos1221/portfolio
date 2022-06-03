from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact, Laboratory, New, Subject, Person, Project, WebTechnology

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Subject)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(WebTechnology)
admin.site.register(Laboratory)
admin.site.register(New)
admin.site.register(Contact)
