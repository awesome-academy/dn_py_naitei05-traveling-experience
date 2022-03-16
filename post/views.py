from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from post.models import Profile

def index(request):
    messages.error(request, _("Your username and password didn't match. Please try again."))
    return render(request, 'index.html')

@login_required
def ProfileDetail(request): 
    user = Profile.objects.filter(username=request.user).first
    context = {
        'user': user,
    }

    return render(request, 'profile/profile_detail.html', context)
