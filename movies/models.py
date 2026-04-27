from django.db import models


class Genre(models.Model):
    # NUEVO
    name = models.CharField(max_length=80, unique=True)
    # CAMBIO: agrego campo descripción
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    synopsis = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    release_date = models.DateField()
    # CAMBIO: agrego URL del póster
    poster_url = models.URLField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    # IMPORTANTE: relación muchos a muchos con Genre
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self) -> str:
        return self.title