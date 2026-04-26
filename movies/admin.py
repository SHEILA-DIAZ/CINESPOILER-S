from django.contrib import admin

from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # NUEVO
    list_display = ("id", "name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # CAMBIO
    list_display = (
        "id",
        "title",
        "duration_minutes",
        "release_date",
        "is_active",
    )
    search_fields = ("title",)
    list_filter = ("is_active", "release_date", "genres")
    filter_horizontal = ("genres",)