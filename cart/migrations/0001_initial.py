# Generated by Django 2.2.10 on 2021-01-06 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=15, verbose_name='Código')),
                ('amount', models.IntegerField(default=0, verbose_name='Descuento Fijo')),
                ('percentage', models.IntegerField(default=0, verbose_name='Porcentaje')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/Inactivo')),
            ],
            options={
                'verbose_name': 'Cupon',
                'verbose_name_plural': 'Cupones',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(default='Vacio', max_length=255, verbose_name='Modelo')),
                ('size', models.CharField(default='Vacio', max_length=255, verbose_name='Talle')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.Producto')),
            ],
            options={
                'verbose_name': 'Articulo Pedido',
                'verbose_name_plural': 'Articulos Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_code', models.IntegerField(default=1000)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PE', 'Pendiente'), ('PR', 'Proceso'), ('FI', 'Finalizado'), ('CA', 'Cancelado')], default='PE', max_length=2, verbose_name='Estado')),
                ('total', models.IntegerField(default=0, verbose_name='Total a Pagar')),
                ('items', models.ManyToManyField(to='cart.OrderItem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
