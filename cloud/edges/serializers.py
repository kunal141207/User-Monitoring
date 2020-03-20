from rest_framework import serializers
from edges.models import Edge

#Edge serializer
class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = '__all__'