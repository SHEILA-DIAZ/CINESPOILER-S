from rest_framework import viewsets

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filterset_fields = ("is_active", "release_date")
    search_fields = ("title", "synopsis")
    ordering_fields = ("title", "release_date", "duration_minutes", "created_at")
    ordering = ("title",)