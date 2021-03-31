from django.views.generic import ListView

from perpustakaan.models import Buku

class BukuList(ListView):
    paginate_by = 5
    model = Buku