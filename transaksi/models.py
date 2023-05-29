from django.db import models
from customer.models import Customer
from user.models import User

class Transaksi(models.Model):
    STATUS_CHOICES = (
        ('baru', 'Baru'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai'),
        ('diambil', 'Diambil'),
    )

    PEMBAYARAN_CHOICES = (
        ('dibayar', 'Dibayar'),
        ('belum_dibayar', 'Belum Dibayar'),
    )

    no_faktur = models.IntegerField()
    id_cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tgl_masuk = models.DateTimeField()
    batas_waktu = models.DateTimeField()
    tgl_bayar = models.DateTimeField()
    jumlah = models.IntegerField()
    harga = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    dibayar = models.CharField(max_length=15, choices=PEMBAYARAN_CHOICES)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    jumlah_bayar = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.jumlah_bayar = self.jumlah * self.harga
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.no_faktur)
    
    class Meta:
        db_table = 'tb_transaksi'
