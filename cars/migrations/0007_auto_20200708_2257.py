# Generated by Django 3.0.5 on 2020-07-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20200708_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getmycars',
            old_name='year',
            new_name='carYear',
        ),
    ]