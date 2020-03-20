from rest_framework import routers
from .api import EdgeViewSet

router = routers.DefaultRouter()
router.register('api/edges', EdgeViewSet, 'edges' )

urlpatterns = router.urls