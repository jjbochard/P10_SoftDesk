from app.models import Comment, Contributor, Issue, Project
from rest_framework.serializers import ModelSerializer


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "id",
            "role",
            "user",
            "project",
        ]
        extra_kwargs = {
            "project": {"read_only": True},
            "id": {"read_only": True},
            "role": {"read_only": True},
        }


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project",
            "author",
            "assignee",
            "comments",
            "created_time",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "author": {"read_only": True},
            "project": {"read_only": True},
            "comments": {"read_only": True},
            "created_time": {"read_only": True},
        }


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "user",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True, "many": True},
        }


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "author",
            "issue",
            "created_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "author": {"read_only": True},
            "issue": {"read_only": True},
            "created_time": {"read_only": True},
        }
