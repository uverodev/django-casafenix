# Generated by Django 2.2 on 2020-07-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.IntegerField(default=1000),
        ),
    ]