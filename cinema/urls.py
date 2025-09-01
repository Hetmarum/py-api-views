from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    CinemaHallViewSet,
    MovieViewSet,
    GenreAPIView,
    ActorGenericAPIView
)

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")


urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list-create"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list-create"),
    path("", include(router.urls)),
]

app_name = "cinema"
