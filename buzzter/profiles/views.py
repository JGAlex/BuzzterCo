# -*- coding: utf-8 -*-

from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render
def ProfileView(request, user_name):
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user})