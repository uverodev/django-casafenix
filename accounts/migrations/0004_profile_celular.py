# Generated by Django 2.2 on 2020-06-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200626_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='celular',
            field=models.TextField(blank=True, max_length=12, null=True, verbose_name='Celular'),
        ),
    ]