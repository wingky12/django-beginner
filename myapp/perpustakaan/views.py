from django.shortcuts import render,redirect
from django.http import HttpResponse
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm






@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Berhasil Dibuat!")
            return redirect('signup')
        else:
            messages.error(request,"terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form
        }
        return render(request,'signup.html', konteks)
        




@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete() 
    messages.success(request,"Data Berhasil di hapus")
    return redirect('buku')


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah_buku.html'
    if request.POST:
        form = FormBuku(request.POST,instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil di perbaharui")
            return redirect("ubah_buku",id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku,
        }
    return render(request, template,konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # return HttpResponse("ini home") #coba
    # books = Buku.objects.filter(jumlah=100) #select * from buku where jumlah = 100
    # books = Buku.objects.filter(kelompok__nama='teknik')[:5] #select * from perpustakaan_buku as a inner join perpustakaan_kelompok as b where a.kelompok_id = b.id and  b.nama='teknik' limit 5;
    books = Buku.objects.all() # select * from buku
    konteks = {
        'books':books
    }
    return render(request,'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request,'penerbit.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form =  FormBuku(request.POST)
        if form.is_valid():
                form.save()
                form = FormBuku()
                pesan = "Data Berhasil Disimpan"
                konteks = {
                    'form':form,
                    'pesan': pesan
                }
                return render(request,'tambah-buku.html',konteks)
    else:
        form = FormBuku()
        konteks ={
            'form': form
        }
        return render(request,'tambah-buku.html', konteks)