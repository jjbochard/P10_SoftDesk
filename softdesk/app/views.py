from app.models import Comment, Contributor, Issue, Project
from app.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])


class UserViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
