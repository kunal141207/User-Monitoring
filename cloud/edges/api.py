from edges.models import Edge, Image, File
from rest_framework import viewsets, permissions
from .serializers import EdgeSerializer, ImageSerializer, FileSerializer

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

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer
    
