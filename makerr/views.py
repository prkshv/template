from django.shortcuts import render
from django.http import HttpResponse
from homee.models import roleassign
# Create your views here.
def dash(request):
    if request.user.is_authenticated:
        return render(request,'makerr/dash.html')
    else:
        return HttpResponse("<h1>Login to access this page</h1>")

def profile(request):
    return render(request,"makerr/profile.html")