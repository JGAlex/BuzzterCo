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