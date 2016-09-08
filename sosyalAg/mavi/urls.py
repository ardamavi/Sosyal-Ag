from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post', views.post, name="post"),
    url(r'^girisYap', views.girisYap, name="girisYap"),
    url(r'^cikisYap', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^uyeOl', views.uyeOl, name="uyeOl"),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name="edit"),
    url(r'^sil/(?P<id>\d+)/$', views.delete, name="sil"),
]
