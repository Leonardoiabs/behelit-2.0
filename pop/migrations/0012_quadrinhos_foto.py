# Generated by Django 4.1.7 on 2023-04-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0011_livros'),
    ]

    operations = [
        migrations.AddField(
            model_name='quadrinhos',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]