# Generated by Django 5.1.6 on 2025-02-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registretion', '0002_myuser_aime'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
