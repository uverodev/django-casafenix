# Generated by Django 2.2.10 on 2020-06-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20200620_0154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-orden', 'fecha_creacion'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default='titulo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen de Presentación'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Segunda Imagen'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Tercera Imagen'),
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default='titulo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_categoria',
            field=models.ManyToManyField(related_name='get_categoria', to='productos.Categoria'),
        ),
    ]