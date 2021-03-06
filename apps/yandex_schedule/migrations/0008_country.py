# Generated by Django 3.1.7 on 2021-09-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_schedule', '0007_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование страны')),
                ('yandex_country_code', models.CharField(max_length=50, unique=True, verbose_name='Код страны Яндекса')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
    ]
