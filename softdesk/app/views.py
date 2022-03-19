from app.models import Comment, Contributor, Issue, Project
from app.permissions import IsAuthor
from app.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ProjectViewset(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsAuthor)

    def get_queryset(self):
        return Project.objects.filter(contributor__user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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
