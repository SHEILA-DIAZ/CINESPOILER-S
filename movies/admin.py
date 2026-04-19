from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration_minutes", "release_date", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active", "release_date")