from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')

def gallery(request):
    return render_to_response('gallery.html')

def video(request):
    return render_to_response('video.html')

def forum(request):
    return render_to_response('forum.html')

def contact(request):
    return render_to_response('contact.html')

def login(request):
    return render_to_response('login.html')

