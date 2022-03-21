from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from post.forms import PostForm
from post.models import Post, Profile

def index(request):
    messages.error(request, _("Your username and password didn't match. Please try again."))
    return render(request, 'index.html')

@login_required
def profile_detail(request): 
    user = Profile.objects.filter(username=request.user).first

    context = {
        'user': user,
    }

    return render(request, 'profile/profile_detail.html', context)

@login_required
def user_management(request): 
    users = Profile.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'admin/user_management.html', context)

@login_required
def post_create(request):
    user = Profile.objects.filter(username=request.user).first()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post()
            post.image = form.cleaned_data["image"]
            post.user = user
            post.content = form.cleaned_data["content"]
            post.title = form.cleaned_data["title"]
            post.save()
        else:
            messages.error(request, _("ERROR: New post creation failed"))
    else:
        form = PostForm(initial={
                    "user": user,
                })

    return render(request, 'post/create_post.html', context={"form": form})
