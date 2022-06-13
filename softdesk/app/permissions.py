from app.models import Contributor
from rest_framework.permissions import BasePermission

author_methods = ("PUT", "DELETE")
contributor_methods = ("POST", "GET")


class HasProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if Contributor.objects.filter(
            project_id=obj.id, user=request.user.id, role="AUTHOR"
        ).exists():
            return True

        if (
            Contributor.objects.filter(
                project_id=obj.id, user=request.user.id, role="ASSIGNEE"
            ).exists()
            and request.method not in author_methods
        ):

            return True

        return False


class HasContributorPermission(BasePermission):
    def has_permission(self, request, view):
        if (
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs["project_pk"], role="AUTHOR")
            .exists()
        ):
            return True

        if (
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs["project_pk"], role="ASSIGNEE")
            .exists()
            and request.method == "GET"
        ):
            return True

    def has_object_permission(self, request, view, obj):
        if (
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs["project_pk"], role="AUTHOR")
            .exists()
        ):
            return True

        if (
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs["project_pk"], role="ASSIGNEE")
            .exists()
            and request.method not in author_methods
        ):
            return True

        return False


class HasIssuePermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            Contributor.objects.filter(
                user=request.user,
                project=view.kwargs["project_pk"],
            ).exists()
        )

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user and request.method in author_methods:
            return True
        return bool(
            (
                Contributor.objects.filter(
                    user=request.user,
                    project=view.kwargs["project_pk"],
                ).exists()
                and request.method in contributor_methods
            )
        )


class HasCommentPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs["project_pk"])
            .exists()
        )

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user and request.method in author_methods:
            return True

        return bool(
            (
                Contributor.objects.filter(
                    user=request.user,
                    project=view.kwargs["project_pk"],
                ).exists()
                and request.method in contributor_methods
            )
        )
