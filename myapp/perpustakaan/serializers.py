from perpustakaan.models import Kelompok
from rest_framework import serializers

class KelompokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields =['id','nama','keterangan']
