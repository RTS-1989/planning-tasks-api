# Generated by Django 3.1.7 on 2021-07-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_schedule', '0004_auto_20210708_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='station_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Яндекс код станции'),
        ),
    ]
