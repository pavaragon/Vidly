from django.db import models
from tastypie.resources import ModelResource, ALL
from rental.models import Movie, Genre
from tastypie.authorization import Authorization 

# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ['title', 'release_year', 'price']
        fltering = {
            'release_year': ALL,
            'price' : ALL,
            'title' : ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete' , 'options']
        authorization = Authorization()

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete' , 'options']
        authorization = Authorization()


"""

Ordering:
/movies/?order_by=price


Filtering:

/movies/?price_lt=10
/movies/?price_gt=10
/movies/?price=10

/movies/?release_year_gt=2018
/movies/?title_contains=tiger



"""