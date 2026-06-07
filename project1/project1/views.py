from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from artikel.models import Kategori, ArtikelBlog

def index(request):
    template_name = "landingpage/index.html"  # Berikan path folder 'landingpage/' di sini
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    print(request.user)  # Menampilkan informasi pengguna yang sedang login di console)

    context = {
        "title": "selamat datang",
        "kategori": kategori,
        "artikel": artikel,
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    artikel = ArtikelBlog.objects.get(id=id)

    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)

    context = {
        "title": "selamat datang",
        "artikel": artikel,
        "artikel_lainnya": artikel_lainnya
    }
    return render(request, template_name, context)

def galeri(request):
    return render(request, 'galeri.html')

def kontak(request):
    return render(request, 'kontak.html')
    
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')

    template_name = "dashboard/index.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title": "selamat datang"
    }
    return render(request, template_name, context)