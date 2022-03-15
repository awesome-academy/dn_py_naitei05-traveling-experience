from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext as _

def index(request):
    messages.error(request, help_text=_("Your username and password didn't match. Please try again."))
    return render(request, 'index.html')
