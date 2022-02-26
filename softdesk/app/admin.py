from app.models import Comment, Contributor, Issue, Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "type",
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "user",
        "role",
    )


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "tag",
        "priority",
        "status",
        "project",
        "author",
        "assignee",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "author",
        "issue",
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
