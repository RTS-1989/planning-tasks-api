# Generated by Django 3.1.7 on 2021-04-22 04:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='taskcategory',
            options={'verbose_name': 'Категория задач', 'verbose_name_plural': 'Категории задач'},
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Задачи на дату'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks_planning.taskcategory', verbose_name='Категория'),
        ),
    ]
