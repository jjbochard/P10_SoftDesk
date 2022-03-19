from app.models import Contributor
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if Contributor.objects.filter(
            project_id=obj.id, user=request.user.id, role="AUTHOR"
        ):
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if (
            Contributor.objects.filter(
                project_id=obj.id, user=request.user.id, role="ASSIGNEE"
            )
            and request.method not in self.edit_methods
        ):
            return True

        return False
