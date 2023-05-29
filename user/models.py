from django.db import models

class User(models.Model):
    id_user = models.CharField(max_length=5)
    nama_user = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tb_user'