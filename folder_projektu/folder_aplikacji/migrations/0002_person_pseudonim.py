# Generated by Django 5.1.2 on 2025-01-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pseudonim',
            field=models.CharField(default='', max_length=80),
        ),
    ]
