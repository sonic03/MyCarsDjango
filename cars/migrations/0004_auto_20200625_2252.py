# Generated by Django 3.0.5 on 2020-06-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200624_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getmycars',
            name='price',
            field=models.IntegerField(verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='getmycars',
            name='year',
            field=models.IntegerField(verbose_name='Yıl'),
        ),
    ]
