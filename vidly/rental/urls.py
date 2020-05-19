from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homePage'),
    path('home', views.index, name='homePage'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('details', views.details, name='details'),
    path('user/login', views.soon , name='login'),
    path('order', views.soon, name='order'),
    path('movie/<int:movie_id>', views.details, name='details'),
]
