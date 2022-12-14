from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    permission_classes=[permissions.AllowAny] #AllowAny -> Permisos a todos a nuestra api #IsAuthenticated
    serializer_class = ProjectSerializer

     