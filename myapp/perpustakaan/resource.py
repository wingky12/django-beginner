from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok__nama', column_name='kelompok')
    class Meta:
        model = Buku
        fields = ['judul','cover','tanggal','kelompok_id__nama','penerbit','jumlah']
        export_order = ['tanggal','kelompok_id__nama','judul','penerbit','jumlah']