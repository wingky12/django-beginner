from django.shortcuts import render,redirect
from django.http import HttpResponse
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

from perpustakaan.data_buku import BukuList

from django.contrib.auth import authenticate

from perpustakaan.resource import BukuResource

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=buku.xls'
    return response






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
        form = FormBuku(request.POST,request.FILES, instance=buku)
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
    paginator = Paginator(books,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    


    konteks = {
        'books' :page_obj,
        # 'level' :level,
        # 'keterangan' : ket
    }
    return render(request,'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request,'penerbit.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form =  FormBuku(request.POST, request.FILES)
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

# def usertest(request):
#     user = authenticate(username='wingky', password='bedoels12')
#     if user is not None:
#         # A backend authenticated the credential
        
#         if user.is_superuser :
#             level = "superadmin"
#             ket = "super admin"
#         else:
#             if user.is_staff:
#                 level = "staff"
#                 ket = "staff"
#             else:
#                 level = "no_staff"
#                 ket = "bukan staff"

#     else:
#     # No backend authenticated the credentials
#         level = "not_found"
#         ket = "tidak ditemukan"
    
#     status ={
#         'level': level,
#         'keterangan': ket
#     }

#     return render(request,"usertest.html",status)

def pdf_download(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
