from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    # NUEVO
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
    # NUEVO: búsqueda por nombre de género
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
    # NUEVO: filtrado y búsqueda
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # NUEVO: filtrar por género
    filterset_fields = ["genres"]
    # NUEVO: buscar por título y sinopsis
    search_fields = ["title", "synopsis"]