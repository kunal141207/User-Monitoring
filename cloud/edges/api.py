from edges.models import Edge
from rest_framework import viewsets, permissions
from .serializers import EdgeSerializer

# Edge Viewset 
class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EdgeSerializer
