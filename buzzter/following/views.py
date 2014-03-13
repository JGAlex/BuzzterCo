# Create your views here.

#"following" es el nombre del paquete dentro del template


from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect

def ProfileFollowingView(request, user_name):
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404
    if request.user == user:
        return FollowersView(request)
    return render(request, "following/profileFollowings.html", {'following':user.profile.followings.all(), 'usuario':user.profile})

def ProfileFollowersView(request, user_name):
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404
    if request.user == user:
        return FollowersView(request)
    return render(request, "following/profileFollowers.html", {'followers':user.profile.followers.all(), 'usuario':user.profile})       
    
def FollowersView(request):
    user = request.user
    if user.is_authenticated():
        return render(request, "following/follower.html")
    
def FollowingView(request):
    user = request.user
    if user.is_authenticated():
        return render(request, "following/following.html")

def Follow(request, username):
    user = User.objects.get(username = username)
    prof = request.user.profile
    
    if user:
        prof.followings.add(user)
        user.profile.followers.add(prof.usuario)
        prof.save()
        user.save()
        return HttpResponseRedirect('/Accounts/'+username+'/')
    
def Unfollow(request, username):
    user = User.objects.get(username = username)
    prof = request.user.profile
    
    if user:
        prof.followings.remove(user)
        user.profile.followers.remove(prof.usuario)
        prof.save()
        user.save()
        return HttpResponseRedirect('/Accounts/'+username+'/')