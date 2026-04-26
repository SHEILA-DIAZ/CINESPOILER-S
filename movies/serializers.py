from rest_framework import serializers

from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    # NUEVO
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
            "is_active",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class MovieSerializer(serializers.ModelSerializer):
    # NUEVO
    genres = GenreSerializer(many=True, read_only=True)

    # NUEVO
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        required=False,
        source="genres",
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "synopsis",
            "duration_minutes",
            "release_date",
            "is_active",
            "genres",
            "genre_ids",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_duration_minutes(self, value: int) -> int:
        if value <= 0:
            raise serializers.ValidationError(
                "Duration must be greater than zero."
            )
        return value