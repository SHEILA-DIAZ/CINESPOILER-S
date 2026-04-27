from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # CAMBIO: prefijo api/v1/ en lugar de api/
    path("api/v1/", include("movies.urls")),
]
