from django.conf import settings
from django.db import models

PERMISSION_CHOICES = ()


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")


class Contributor(models.Model):
    role = models.CharField(max_length=100)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Issue(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)