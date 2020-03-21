from edges.models import Edge, Image
from rest_framework import viewsets, permissions
from .serializers import EdgeSerializer, ImageSerializer

# Edge Viewset 
class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EdgeSerializer

# Image Viewset 
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer
