from rest_framework.viewsets import ModelViewSet
from anime.models import Anime
from .serializers import AnimeSerializer

class AnimeViewSet(ModelViewSet):

    queryset = Anime.objects.all()

    serializer_class = AnimeSerializer