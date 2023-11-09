from rest_framework.serializers import ModelSerializer
from ..models import RelatedPost

class RelatedPostSerializer(ModelSerializer):
    class Meta:
        model = RelatedPost
        fields = ('id', 'title', 'image',)
