# Generated by Django 2.2.10 on 2021-01-06 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('spouse_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('document', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=220, null=True, verbose_name='Apellidos')),
                ('region', models.CharField(choices=[('PY01', 'Concepcion'), ('PY02', 'San Pedro'), ('PY03', 'Cordillera'), ('PY04', 'Guaira'), ('PY05', 'Caaguazu'), ('PY06', 'Caazapa'), ('PY07', 'Itapua'), ('PY08', 'Misiones'), ('PY09', 'Paraguari'), ('PY10', 'Alto Parana'), ('PY11', 'Central'), ('PY12', 'Neembucu'), ('PY13', 'Amambay'), ('PY14', 'Canindeyu'), ('PY15', 'Presidente Hayes'), ('PY16', 'Boqueron'), ('PY17', 'Alto Paraguay')], max_length=4, verbose_name='Departamento')),
                ('city', models.CharField(blank=True, max_length=220, null=True, verbose_name='Ciudad')),
                ('celular', models.TextField(blank=True, max_length=10, null=True, verbose_name='Celular:')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-document'],
            },
        ),
    ]
