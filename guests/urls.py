from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddGuestView.as_view(), name='index'),
    path('deleteguest/', views.DeleteGuestView.as_view(), name='deleteguest'),
    path('deleteguest/<int:guest_id>/', views.DeleteGuestView.as_view(), name='deleteguest')
]
