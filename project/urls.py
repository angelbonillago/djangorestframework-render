#rest_framework tiene un modulo para crear mis rutas

from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() #generamos la url CRUD para la api.

router.register('api/projects',ProjectViewSet,'projects')

urlpatterns=router.urls
