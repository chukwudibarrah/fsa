from rest_framework.viewsets import ModelViewSet
from . serializers import ProjectSerializer
from .. models import Project

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer