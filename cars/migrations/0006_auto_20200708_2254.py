# Generated by Django 3.0.5 on 2020-07-08 19:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_getmycars_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gearName', models.CharField(max_length=120, verbose_name='Vites')),
            ],
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markaName', models.CharField(max_length=120, verbose_name='marka')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=120, verbose_name='model')),
            ],
        ),
        migrations.AddField(
            model_name='getmycars',
            name='year',
            field=models.IntegerField(default=1, verbose_name='Yıl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmycars',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.Model', verbose_name='Model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='getmycars',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Gear', verbose_name='Vites'),
        ),
        migrations.AlterField(
            model_name='getmycars',
            name='marka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Marka', verbose_name='Marka'),
        ),
    ]
