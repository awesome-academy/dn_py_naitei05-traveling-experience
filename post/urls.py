from django.urls import include, path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.ProfileDetail, name='profile-detail'),
]
