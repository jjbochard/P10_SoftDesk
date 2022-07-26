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
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
    )
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")

    def __str__(self):
        return self.title


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
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contributors",
    )

    class Meta:
        unique_together = ["user", "project", "role"]

    def __str__(self):
        return f"{self.user.__str__()}_{self.project.__str__()}"


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
    INPROGRESS = "PROGRESS"
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
        max_length=8,
        choices=STATUS_CHOICES,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues"
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_issues",
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_issues",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
