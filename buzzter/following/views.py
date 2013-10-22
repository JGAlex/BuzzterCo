# Create your views here.

#"following" es el nombre del paquete dentro del template


from django.shortcuts import render

def FollowingView(request):
    user = request.user
    if user.is_authenticated():
        return render(request, "following/following.html")
    
def FollowersView(request):
    user = request.user
    if user.is_authenticated():
        return render(request, "following/follower.html")

def Follow(request, username):
    user = User.objects.get(username = username)
    prof = request.user.profile
    if user:
        prof.followings.add(user)
        user.profile.followers.add(prof.usuario)
        prof.save()
        user.save()
        return render(request, "following/following.html")
    
def Unfollow(request, username):
    user = User.objects.get(username = username)
    prof = request.user.profile
    
    if user:
        prof.followings.remove(user)
        user.profile.followers.remove(prof.usuario)
        prof.save()
        user.save()
        return render(request, "following/following.html")