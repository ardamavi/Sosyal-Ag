from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.views.generic import View
import sqlite3
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    post_list = Post.objects.all()[::-1]
    paginator = Paginator(post_list, 100)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'posts': posts})

def post(request):
    metin = request.POST['metin']
    if metin == "":
        messages.add_message(request, messages.INFO, "Metin boş geçilemez !")
    else:
        Post(name=request.user.username, first_name=request.user.first_name, last_name=request.user.last_name, text=metin).save()
        messages.add_message(request, messages.INFO, "<span style='color: green;'>Paylaşıldı!</span>")

    return redirect("mavi:index")

def girisYap(request):
    kullaniciAdi = request.POST['kullaniciAdi']
    sifre = request.POST['sifre']
    if kullaniciAdi == "" or sifre == "":
        messages.add_message(request, messages.INFO, "Alanlar boş bırakılamaz !")
    else:
        user = authenticate(username=kullaniciAdi, password=sifre)
        if user is not None:
            login(request, user)
    return redirect("mavi:index")

def kullaniciAdiKntrl(ad):
    if " " in ad:
        return False

    return True

def uyeOl(request):
    kullaniciAdi = request.POST['kullaniciAdi']
    sifre = request.POST['sifre']
    sifre2 = request.POST['sifre2']
    adi = request.POST["adi"]
    soyadi = request.POST["soyadi"]

    if kullaniciAdi == "" or sifre == "" or sifre2 == "" or adi == "" or soyadi == "":
        messages.add_message(request, messages.INFO, "Alanlar boş bırakılamaz!")
    elif sifre != sifre2:
        messages.add_message(request, messages.INFO, "2. Şifre hatalı!")
    elif kullaniciAdiKntrl(kullaniciAdi) == False:
        messages.add_message(request, messages.INFO, "Kullanıcı adı; kelimeler, rakamlar ve @/./+/-/_ karakterlerinden oluşabilir, 30 karakter veya daha az olamalıdır!")
    else :
        user = User(username=kullaniciAdi, first_name=adi, last_name=soyadi, is_staff=False)
        user.set_password(sifre)
        user.save()
        messages.add_message(request, messages.INFO, "<span style='color: green;'>Giriş yapabilirsiniz!</span>")

    return redirect("mavi:index")
