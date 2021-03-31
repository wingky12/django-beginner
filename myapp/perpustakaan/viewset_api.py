from perpustakaan.models import *
from perpustakaan.serializers import KelompokSerializer
from rest_framework import viewsets

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all() # 
    serializer_class = KelompokSerializer