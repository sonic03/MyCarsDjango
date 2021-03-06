# Generated by Django 3.0.5 on 2020-06-23 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='getmycars',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='gear',
            field=models.CharField(choices=[('manuel', 'Manuel'), ('otomatik', 'Otomatik')], default=django.utils.timezone.now, max_length=20, verbose_name='Vites'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='km',
            field=models.IntegerField(default=1, verbose_name='Kilometre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='marka',
            field=models.CharField(choices=[('alfa_romeo', 'Alfa Rome'), ('tofas', 'Tofaş')], default='Bir marka seçin', max_length=30),
        ),
        migrations.AddField(
            model_name='getmycars',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='price',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20, verbose_name='Fiyat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='year',
            field=models.DecimalField(decimal_places=2, default=1 ,max_digits=4, verbose_name='Yıl'),
            preserve_default=False,
        ),
    ]
