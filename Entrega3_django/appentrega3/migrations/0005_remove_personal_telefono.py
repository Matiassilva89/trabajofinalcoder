# Generated by Django 4.2.6 on 2023-11-11 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appentrega3', '0004_personal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='telefono',
        ),
    ]