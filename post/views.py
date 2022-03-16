from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from post.models import Profile

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
