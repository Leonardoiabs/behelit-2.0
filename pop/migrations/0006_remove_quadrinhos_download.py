# Generated by Django 4.1.7 on 2023-03-28 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quadrinhos',
            name='download',
        ),
    ]