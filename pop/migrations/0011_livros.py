# Generated by Django 4.1.7 on 2023-04-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0010_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('link', models.URLField()),
                ('foto', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('concluído', 'Concluído'), ('em andamento', 'Em andamento'), ('hiatus', 'Hiatus'), ('listado', 'Listado')], max_length=30)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pop.genero')),
            ],
        ),
    ]
