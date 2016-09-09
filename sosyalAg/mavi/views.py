from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .models import guncelYazi
from django.views.generic import View
import sqlite3
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

def index(request):
    post_list = Post.objects.all()[::-1]
    guncelYazilar = guncelYazi.objects.all()
    paginator = Paginator(post_list, 100)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts, 'guncelYazilar': guncelYazilar})

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
        else:
            messages.add_message(request, messages.INFO, "Böyle bir kullanıcı bulunamadı!<br />Lütfen üye olun!")
    return redirect("mavi:index")

def kullaniciAdiKntrl(ad):
    if " " in ad:
        return False
    ozelKarakterler = [".", "-", "_"]
    for harf in ad:
        if harf.isalpha() or harf.isdigit() or (harf in ozelKarakterler):
            continue
        else:
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
        messages.add_message(request, messages.INFO, "Kullanıcı adı; kelimeler, rakamlar ve ./-/_ karakterlerinden oluşabilir, en fazla 30 veya daha az karakter olamalıdır!")
    else :
        try:
            user = User(username=kullaniciAdi, first_name=adi, last_name=soyadi, is_staff=False)
            user.set_password(sifre)
            user.save()
            messages.add_message(request, messages.INFO, "<span style='color: green;'>Giriş yapabilirsiniz!</span>")
        except:
            messages.add_message(request, messages.INFO, "Bu kullanıcı zaten var!")

    return redirect("mavi:index")

def delete(request, id):
    post = get_object_or_404(Post, pk=id).delete()
    messages.add_message(request, messages.INFO, "<span style='color: green;'>Gönderiniz Silindi!</span>")
    return redirect("mavi:index")

def edit(request, id):
    metin = request.POST['metin']
    if metin == "":
        messages.add_message(request, messages.INFO, "Metin boş geçilemez !")
    else:
        post = Post.objects.filter(id=id).update(text = metin)
        messages.add_message(request, messages.INFO, "<span style='color: green;'>Gönderiniz Düzenlendi!</span>")
    return redirect("mavi:index")

def kullaniciPost(request, kullaniciAdi):
    post_list = Post.objects.filter(name=kullaniciAdi)[::-1]
    guncelYazilar = guncelYazi.objects.all()
    paginator = Paginator(post_list, 100)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if post_list == []:
        messages.add_message(request, messages.INFO, "Kullanıcının paylaşımı bulunmamaktadır!")
    else:
        messages.add_message(request, messages.INFO, "<span style='color: #fc4f3f;'>Profil: </span><span style='color:#3377CC; font-size:15px;'>@"+kullaniciAdi+"</span>")

    return render(request, 'index.html', {'posts': posts, 'guncelYazilar': guncelYazilar})
