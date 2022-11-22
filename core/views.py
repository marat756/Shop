from django.shortcuts import render
from core.models import * 

def home(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar': malumotlar
    }
    return render(request, '/home.html')

def good(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar': malumotlar
    }
    return render(request, 'cor/good.html')
 
def make(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar' == malumot
    }
    return render(request, 'cor/gif.html')

def gif(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar' == malumot
    }
    return render(request, 'cor/kok.html')

def kok(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar' == malumot
    }
    return render(request, 'cor/make.html')
