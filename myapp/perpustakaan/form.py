from django.forms import ModelForm
from perpustakaan.models import Buku
from django import forms

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
#        exclude = ['penerbit']
 #       fields = ['judul','penulis','kelompok']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok':forms.Select({'class':'form-control'}),
        }