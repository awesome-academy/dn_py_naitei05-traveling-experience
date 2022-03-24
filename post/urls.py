from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile_detail, name='profile-detail'),
    path('profile-list', views.AuthorListView.as_view(), name='profile-list'),
    path('users', views.user_management, name='user-management'),
    path('create-post', views.post_create, name='create-post'),
    path('post-list', views.PostListView.as_view(), name='post-list'),
    path('post-detail/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
