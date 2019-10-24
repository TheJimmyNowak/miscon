from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddGuest.as_view(), name='index'),
]
