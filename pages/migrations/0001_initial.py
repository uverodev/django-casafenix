# Generated by Django 2.2.10 on 2021-01-06 01:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField(default='')),
                ('orden', models.SmallIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Visible/Invisible')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
                'ordering': ['orden', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Destacado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitulo', models.CharField(max_length=100, verbose_name='Subtitulo')),
                ('orden', models.SmallIntegerField(default=0)),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/Inactivo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('pagina', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pages.Page')),
            ],
            options={
                'verbose_name': 'Destacado',
                'verbose_name_plural': 'Destacados',
                'ordering': ['orden', 'titulo'],
            },
        ),
    ]
