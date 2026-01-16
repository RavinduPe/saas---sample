from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def profile_view(request, *args, **kwargs):
    return HttpResponse("<h1>Profile Page</h1>")    