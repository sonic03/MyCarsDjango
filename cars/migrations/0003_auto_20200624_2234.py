# Generated by Django 3.0.5 on 2020-06-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200623_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='getmycars',
            name='car_img1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel'),
        ),
        migrations.AddField(
            model_name='getmycars',
            name='car_img2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel'),
        ),
        migrations.AddField(
            model_name='getmycars',
            name='car_img3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel'),
        ),
        migrations.AddField(
            model_name='getmycars',
            name='car_img4',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel'),
        ),
    ]
