# Generated by Django 5.0.2 on 2024-06-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]