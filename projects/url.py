from rest_framework import routers
from .api import ProjectyViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectyViewSet, "projects")
urlpatterns = router.urls
