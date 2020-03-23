from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include
from .api import EdgeViewSet, ImageViewSet
from .views import FileUploadView
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register('api/edges', EdgeViewSet, 'edges' )
router.register('api/images', ImageViewSet, 'images' )
#router.register('api/uploads',FileUploadView.as_view(),'uploads')

urlpatterns = [ url(r'^', include(router.urls)),
    url(r'api/uploads',csrf_exempt(FileUploadView.as_view())) ]


    