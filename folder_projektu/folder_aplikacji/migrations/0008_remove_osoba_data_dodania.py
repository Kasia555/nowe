# Generated by Django 5.1.5 on 2025-01-26 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0007_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osoba',
            name='data_dodania',
        ),
    ]