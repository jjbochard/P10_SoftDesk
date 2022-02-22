from re import T
from django.db import models
from django.forms import CharField
from users.models import User
from django.conf import settings


PERMISSION_CHOICES = ()


class Project(models.Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    type = CharField(max_length=255)
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")


class Contributor(models.Model):
    role = CharField(max_length=100)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Issue(models.Model):
    title = CharField(max_length=255, primary_key=True)
    description = CharField(max_length=255)
    tag = CharField(max_length=50)
    priority = CharField(max_length=50)
    status = CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = CharField(max_length=255)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
