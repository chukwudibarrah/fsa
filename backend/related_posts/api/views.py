from rest_framework import generics
from ..models import RelatedPost
from .serializers import RelatedPostSerializer

class RelatedPostList(generics.ListCreateAPIView):
    queryset = RelatedPost.objects.all()
    serializer_class = RelatedPostSerializer
