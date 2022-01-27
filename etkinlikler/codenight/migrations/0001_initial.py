# Generated by Django 4.0.1 on 2022-01-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeNight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100, verbose_name='etkinlik ismi')),
                ('aciklama', models.TextField(verbose_name='etkinlik Açıklaması')),
                ('aktif', models.BooleanField(default=True)),
                ('etkinlik_tarihi', models.DateTimeField(verbose_name='Etkinlik tarihi')),
                ('mekan', models.CharField(max_length=70, verbose_name='Etkinliğin gerçekleştirileceği mekan')),
                ('koordinator', models.CharField(max_length=100, verbose_name='Etkinlik Koordinatörü')),
                ('konu', models.CharField(max_length=100, null=True, verbose_name='Etkinliğin Konusu')),
            ],
        ),
    ]
