from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
