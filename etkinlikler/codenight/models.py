from django.db import models

# Create your models here.

class CodeNight(models.Model):
    isim=models.CharField(max_length=100,verbose_name='etkinlik ismi')
    aciklama=models.TextField(verbose_name='etkinlik Açıklaması')
    aktif=models.BooleanField(default=True)
    etkinlik_tarihi=models.DateTimeField(verbose_name='Etkinlik tarihi')
    mekan=models.CharField(max_length=70,verbose_name='Etkinliğin gerçekleştirileceği mekan')
    koordinator=models.CharField(max_length=100,verbose_name='Etkinlik Koordinatörü')
    konu=models.CharField(max_length=100,verbose_name='Etkinliğin Konusu',null=True)
    def __str__(self):
        return self.isim