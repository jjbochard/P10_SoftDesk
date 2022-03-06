from app.models import Comment, Contributor, Issue, Project
from rest_framework.serializers import ModelSerializer


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


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "role",
            "user",
            "project",
        ]


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "user",
            "issues",
        ]


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
