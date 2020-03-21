from rest_framework import routers
from .api import EdgeViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('api/edges', EdgeViewSet, 'edges' )
router.register('api/images', ImageViewSet, 'images' )

urlpatterns = router.urls