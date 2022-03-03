from app.views import CommentViewset, IssueViewset, ProjectViewset, UserViewset
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register("projects", ProjectViewset, basename="projects")
# generates:
# /projects/
# /projects/{pk}/

project_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
project_router.register("issues", IssueViewset, basename="issues")
project_router.register("users", UserViewset, basename="users")
# generates:
# /projects/{project_pk}/issues/
# /projects/{project_pk}/issues/{issue_pk}/

issues_router = routers.NestedSimpleRouter(project_router, "issues", lookup="issue")
issues_router.register("comments", CommentViewset, basename="comments")
# generates:
# /projects/{project_pk}/issuess/{issue_pk}/comments/
# /projects/{project_pk}/issuess/{issue_pk}/comments/{pk}/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(issues_router.urls)),
]
