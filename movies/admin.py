from django.contrib import admin
from .models import Genre, Movie


# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


# NUEVO
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration_minutes", "release_date", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active", "genres")
    filter_horizontal = ("genres",)