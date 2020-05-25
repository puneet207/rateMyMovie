from django.urls import path
from movie.api.views import(
    create_movie,
    rate_movie,
)

app_name = 'movie'

urlpatterns = [
    path('create', create_movie, name="create"),
    path('rate', rate_movie, name="rate"),
    ]