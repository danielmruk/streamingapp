from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return redirect(stream_home)

@login_required(login_url='/stream/sign-in/')

def stream_home(request):
    return render(request, 'stream/home.html')
