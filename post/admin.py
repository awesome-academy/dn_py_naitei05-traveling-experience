from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Post, Rate, Follow, Tag, Comment

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    model = Follow

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    fields = ['user', 'title', 'content', 'image', 'rate_average', 'status']

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('post', 'point')

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    model = Comment

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
