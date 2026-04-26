from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    # NUEVO
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = ("name",)
    ordering_fields = ("id", "name", "created_at")
    ordering = ("name",)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # CAMBIO
    filterset_fields = ("is_active", "release_date", "genres")
    search_fields = ("title", "synopsis", "genres__name")
    ordering_fields = ("id", "title", "release_date", "duration_minutes", "created_at")
    ordering = ("title",)