from django.conf import settings
from django.db import models


class Project(models.Model):
    FRONTEND = "FRONT"
    BACKEND = "BACK"
    ANDROID = "ANDROID"
    IOS = "IOS"
    TYPE_CHOICES = [
        (FRONTEND, "Front-end"),
        (BACKEND, "Back-end"),
        (ANDROID, "Android"),
        (IOS, "iOS"),
    ]
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
    )
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")

    def __str__(self):
        return self.title

    def get_products(self):
        return "\n".join([p.username for p in self.user.all()])


class Contributor(models.Model):
    AUTHOR = "AUTHOR"
    ASSIGNEE = "ASSIGNEE"
    ROLE_CHOICES = [
        (AUTHOR, "Author"),
        (ASSIGNEE, "Assignee"),
    ]
    role = models.CharField(
        max_length=8,
        choices=ROLE_CHOICES,
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Issue(models.Model):
    BUG = "BUG"
    IMPROVEMENT = "IMPROVE"
    TASK = "TASK"
    TAG_CHOICES = (
        (BUG, "Bug"),
        (IMPROVEMENT, "Improvement"),
        (TASK, "Task"),
    )
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    PRIORITY_CHOICES = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    )
    TODO = "TODO"
    INPROGRESS = "PROGESS"
    DONE = "DONE"
    STATUS_CHOICES = (
        (TODO, "To Do"),
        (INPROGRESS, "In Progress"),
        (DONE, "Done"),
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(
        max_length=7,
        choices=TAG_CHOICES,
    )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
    )
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
