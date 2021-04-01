from django.contrib import admin
from perpustakaan.models import Buku, Kelompok,Negara


# Register your models here.
class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit','jumlah','negara_id']
    search_fields = ['judul', 'penulis','penerbit']
    list_filter = ['kelompok_id']
    list_per_page = 4

class KelompokAdmin(admin.ModelAdmin):
    list_display= ['id','kelompok']
    search_fields = ['kelompok']
    list_per_page = 5

class NegaraAdmin(admin.ModelAdmin):
    list_display=['id','negara']
    search_fields = ['judul', 'penulis','penerbit']
    list_per_page = 5

admin.site.register(Buku,BukuAdmin)
admin.site.register(Kelompok)
admin.site.register(Negara)