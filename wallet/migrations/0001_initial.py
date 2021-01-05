# Generated by Django 2.2.10 on 2020-12-29 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
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
                ('code_transaction', models.IntegerField(default=0)),
                ('date_transaction', models.DateTimeField(auto_now=True)),
                ('code_annulment', models.IntegerField(blank=True, default=0, null=True)),
                ('date_annulment', models.DateTimeField(auto_now=True)),
                ('mount', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile')),
            ],
        ),
    ]