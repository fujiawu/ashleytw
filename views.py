from django.shortcuts import *

def home(request):
        return render(request, 'home.html')
       
def gallery(request):
        return render(request, 'gallery.html')
        
def video(request):
        return render(request, 'video.html')

def forum(request):
        return render(request, 'forum.html')

def family_tree(request):
        return render(request, 'family-tree.html')

def contact(request):
       return render(request, 'contact.html')

def profile(request):
    if request.user.is_authenticated():
        return render(request, 'profile.html')

