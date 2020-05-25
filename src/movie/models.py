from django.db import models
from accounts.models import Accounts



class Movie(models.Model):
    name 				= models.CharField(max_length=50, null=False)
    description 		= models.TextField(max_length=5000, null=False, blank=True)
    date_created 		= models.DateTimeField(auto_now_add=True, verbose_name="date created")
    date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
    created_by 			= models.ForeignKey(Accounts, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Rating(models.Model):
    rating 				= models.FloatField(null=False)
    description 		= models.TextField(max_length=5000, null=False, blank=True)
    date_created 		= models.DateTimeField(auto_now_add=True, verbose_name="date created")
    date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
    movie_id 			= models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating_by 			= models.ForeignKey(Accounts, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

