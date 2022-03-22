from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile_detail, name='profile-detail'),
    path('users', views.user_management, name='user-management'),
    path('create-post', views.post_create, name='create-post'),
]
