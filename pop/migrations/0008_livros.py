# Generated by Django 4.1.7 on 2023-04-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0007_alter_quadrinhos_status_alter_quadrinhos_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('terror', 'Terror'), ('suspense', 'Suspense'), ('sci-fi', 'Sci-fi'), ('fantasia medieval', 'Fantasia Medieval'), ('biografia', 'Biografia'), ('informação', 'Informação'), ('programação', 'Programação')], max_length=30)),
                ('link', models.URLField()),
                ('foto', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('concluído', 'Concluído'), ('em andamento', 'Em andamento'), ('hiatus', 'Hiatus'), ('listado', 'Listado')], max_length=30)),
            ],
        ),
    ]