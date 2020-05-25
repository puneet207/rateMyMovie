from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from accounts.models import Accounts
from movie.models import Movie,Rating
from movie.api.serializers import MovieSerilizer, MovieCreateSerilizer, RatingSerializer


# Url: https://<your-domain>/api/movie/create
# Headers: Authorization: Token <token>

@api_view(['POST',])
@permission_classes((IsAuthenticated, IsAdminUser,))
def create_movie(request):
    data = request.data
    #data['created_by'] = request.user.pk
    serializer = MovieCreateSerilizer(data=data)

    data = {}
    if serializer.is_valid():
        movie = serializer.save()
        data['response'] = 'success'
        data['pk'] = movie.pk
        data['name'] = movie.name
        data['description'] = movie.description
        data['date_updated'] = movie.date_updated
        data['username'] = movie.created_by.username
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Url: https://<your-domain>/api/movie/rate
# Headers: Authorization: Token <token>

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def rate_movie(request):
    data = request.data
    #data['rating_by'] = request.user.pk
    serializer = RatingSerializer(data=data)

    data = {}
    if serializer.is_valid():
        rating_detail = serializer.save()
        data['response'] = 'success'
        data['pk'] = rating_detail.pk
        data['rating'] = rating_detail.rating
        data['movie'] = Movie.object.get(id=rating_detail.movie_id)
        data['description'] = rating_detail.description
        data['date_updated'] = rating_detail.date_updated
        data['username'] = rating_detail.rating_by.username
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

