# Generated by Django 4.1.7 on 2023-04-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0012_quadrinhos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quadrinhos',
            name='foto',
            field=models.ImageField(upload_to='quadrinhos/'),
        ),
    ]
