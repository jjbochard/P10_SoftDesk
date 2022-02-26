from app.models import Project
from app.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectAPIView(APIView):
    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
