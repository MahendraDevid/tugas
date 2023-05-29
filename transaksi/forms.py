from django import forms
from .models import Transaksi

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = ('no_faktur', 'id_cust', 'tgl_masuk', 'batas_waktu', 'tgl_bayar', 'jumlah', 'harga', 'status', 'dibayar', 'id_user', 'jumlah_bayar')