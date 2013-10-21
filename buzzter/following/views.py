# Create your views here.
from django.shortcuts import render

def FollowingView(request):
    user = request.user
    if user.is_authenticated():
        return render(request, "following/following.html")
    
