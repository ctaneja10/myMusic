from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import song
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    all_songs = song.objects.all()
    params = {'all_songs': all_songs}
    return render(request, 'song/index.html', params)

def creationpage(request):
    return render(request, 'song/creation.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('cpass')
        if password != cpass:
            messages.warning(request, "Password does not match")
            return redirect('home')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('pass')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials, please try again')
            return redirect('home')
    return HttpResponse('404 - Not found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('home')

def uploadMusic(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        cover_album=request.POST.get('cover_album')
        audio_file=request.POST.get('audio_file')
        artist_name=request.POST.get('artist_name')
        p = song(name=name, desc=desc, cover_album=cover_album,
                 audio_file=audio_file, artist_name=artist_name)
        p.save()
        return render(request, 'song/upload.html')
    return render(request, 'song/upload.html')

def deleteSong(request, slug):
    allSongs = song.objects.filter(song_slug=slug)
    allSongs.delete()
    return redirect('home')

def song_pg(request):
    all_songs = song.objects.all()
    params = {'all_songs': all_songs}
    return render(request, 'song/song.html', params)

