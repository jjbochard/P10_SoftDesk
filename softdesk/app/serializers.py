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
    user = ContributorSerializer(source="users", read_only=True, many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "user",
        ]

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        Contributor.objects.create(
            project_id=project.id,
            role="AUTHOR",
            user_id=self.context["request"].user.id,
        )
        return project


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
