from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post', views.post, name="post"),
    url(r'^girisYap', views.girisYap, name="girisYap"),
    #url(r'^uyeOl', views.uyeOl, name="uyeOl")
]
