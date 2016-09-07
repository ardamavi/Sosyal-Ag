from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.views.generic import View
import sqlite3
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()[::-1]

def post(request):
    kullaniciAdi = request.POST['kullaniciAdi']
    metin = request.POST['metin']
    if kullaniciAdi == "":
        kullaniciAdi = "Anonim"
    if metin == "":
        messages.add_message(request, messages.INFO, "! Metin Boş Geçilemez !")
    else:
        conn = sqlite3.connect("db.sqlite3")
        db = conn.cursor()
        db.execute("INSERT INTO mavi_post VALUES (NULL ,'{0}','{1}')".format(kullaniciAdi, metin))
        if conn:
            conn.commit()
            conn.close()
    return redirect("mavi:index")

def girisYap(request):
    kullaniciAdi = request.POST['kullaniciAdi']
    sifre = request.POST['sifre']
    if kullaniciAdi == "" or sifre == "":
        messages.add_message(request, messages.INFO, "! Alanlar Boş Bırakılamaz !")
    else:
        user = authenticate(username=kullaniciAdi, password=sifre)
        if user is not None:
            login(request, user)
    return redirect("mavi:index")
