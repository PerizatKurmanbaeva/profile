# Generated by Django 4.0.6 on 2022-07-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name='Дата рождения'),
        ),
    ]