from app.models import Comment, Contributor, Issue, Project
from app.permissions import (
    HasCommentPermission,
    HasContributorPermission,
    HasIssuePermission,
    HasProjectPermission,
)
from app.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)
from rest_framework import status
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomViewset(
    GenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    pass


class ProjectViewset(CustomViewset):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, HasProjectPermission)
    http_method_names = ["post", "get", "put", "delete"]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            contributor = Contributor.objects.create(
                project=project,
                role="AUTHOR",
                user=request.user,
            )
            contributor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueViewset(CustomViewset):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, HasIssuePermission)
    http_method_names = ["post", "get", "put", "delete"]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs["project_pk"])
        serializer = IssueSerializer(data=request.data)
        if Contributor.objects.filter(
            user=request.data["assignee"],
            project=project,
        ).exists():
            if serializer.is_valid():
                serializer.save(author=request.user, project=project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = "The assignee user is not a contributor of this project"
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)


class CommentViewset(CustomViewset):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, HasCommentPermission)
    http_method_names = ["post", "get", "put", "delete"]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])

    def create(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs["issue_pk"])
        project = Project.objects.get(id=kwargs["project_pk"])
        serializer = CommentSerializer(data=request.data)
        if (
            Contributor.objects.filter(user=request.user)
            .filter(project=project)
            .exists()
        ):
            if serializer.is_valid():
                serializer.save(author=request.user, issue=issue)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(CustomViewset):
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated, HasContributorPermission)
    http_method_names = ["post", "get", "delete"]
    lookup_field = "user_id"

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs["project_pk"])
        serializer = ContributorSerializer(data=request.data)
        user = request.data["user"]
        if Contributor.objects.filter(user=user).filter(project=project).exists():
            message = f"The user {user} is already related to the project {project.id}"
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save(project=project, role="ASSIGNEE")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.role == "AUTHOR":
            message = "You can't delete the author of a project"
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
