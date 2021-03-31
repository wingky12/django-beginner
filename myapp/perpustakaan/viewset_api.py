from perpustakaan.models import *
from perpustakaan.serializers import KelompokSerializer
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here


class KelompokViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = Kelompok.objects.all() # 
    serializer_class = KelompokSerializer

