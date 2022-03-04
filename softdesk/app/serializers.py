from app.models import Comment, Contributor, Issue, Project
from rest_framework.serializers import ModelSerializer, ValidationError


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
            "id",
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

    def validate_title(self, value):
        if Project.objects.filter(title=value).exists:
            raise ValidationError("Project already exists")
        return value


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
