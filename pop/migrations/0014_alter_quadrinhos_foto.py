# Generated by Django 4.1.7 on 2023-04-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0013_alter_quadrinhos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quadrinhos',
            name='foto',
            field=models.ImageField(null=True, upload_to='quadrinhos/'),
        ),
    ]
