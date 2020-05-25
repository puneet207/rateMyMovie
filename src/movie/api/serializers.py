from rest_framework import serializers
from movie.models import Movie,Rating


class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'date_created', 'date_updated', 'created_by']



class MovieCreateSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['name', 'description', 'date_created', 'date_updated', 'created_by']

    def save(self):
        try:
            movie = Movie(
                name = self.validated_data['name'],
                description = self.validated_data['description'],
                created_by = self.validated_data['created_by'],
            )
            movie.save()
            return movie
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a name, some content, and created by."})


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['rating', 'description', 'date_created', 'date_updated', 'movie_id', 'rating_by']

    def save(self):
        try:
            rating_details = Rating.objects.get(rating_by=self.validated_data['rating_by'])
            if rating_details.movie_id == self.validated_data['movie_id'] :
                raise serializers.ValidationError({"response": "You have already rated for {0} movie".format(self.validated_data['movie_id'])})
            rating_detail = Rating(
                rating = self.validated_data['name'],
                description = self.validated_data['description'],
                rating_by = self.validated_data['rating_by'],
                movie_id = self.validated_data['movie_id'],
            )
            rating_detail.save()
            return rating_detail

        except KeyError:
            pass
