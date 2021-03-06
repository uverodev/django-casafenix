# Generated by Django 2.2.10 on 2021-01-06 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('concept', models.CharField(max_length=100)),
                ('code_transaction', models.IntegerField(default=0)),
                ('date_transaction', models.DateTimeField(auto_now=True)),
                ('code_annulment', models.IntegerField(blank=True, default=0, null=True)),
                ('date_annulment', models.DateTimeField(auto_now=True)),
                ('mount', models.IntegerField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Order')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
            ],
        ),
    ]
