# Generated by Django 5.0.2 on 2024-06-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_forms_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
