from app.models import Comment, Contributor, Issue, Project
from app.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ProjectViewset(
    GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin
):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(
            contributor__role="AUTHOR", contributor__user=self.request.user
        )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])


class UserViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
