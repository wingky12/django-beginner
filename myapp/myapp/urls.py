"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#ini untuk routing awal di def index dibawah ini
from django.http import HttpResponse

from perpustakaan.views import *
#from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static #panggil media ke url

#def buku(request):
#	return HttpResponse("buku")

def index(request):
	return HttpResponse("halaman depan")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
 #   path('buku/', buku),
  #  path('about', views.about, name='about')

    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit,name='penerbit'),
    path('tambah-buku/',tambah_buku,name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>',hapus_buku,name='hapus_buku'),
    path('masuk',LoginView.as_view(), name='masuk'),
    path('keluar/',LogoutView.as_view(next_page='masuk'),name='keluar'),
    path('signup/',signup, name='signup'),
    path('export/xls', export_xls, name='export_xls'),
    # path('usertest', usertest, name='usertest'),
      path('pdf/', pdf_download, name='pdf_download')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)