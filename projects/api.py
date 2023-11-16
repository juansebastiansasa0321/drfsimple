from projects.models import Project
from rest_framework import viewsets,permissions
from .serieelizers import Projectserializer

class ProjectyViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Projectserializer

