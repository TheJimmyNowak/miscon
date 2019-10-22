from django.urls import path

from . import views

urlpatterns = [
    path('', views.rent, name='index'),
    path('give-back', views.give_back, name='give-back')
]
