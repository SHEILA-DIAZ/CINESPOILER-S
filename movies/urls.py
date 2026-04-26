from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet  # IMPORTANTE

router = DefaultRouter()

router.register(r"genres", GenreViewSet, basename="genre")  # NUEVO
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = router.urls